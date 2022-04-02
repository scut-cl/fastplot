# -*- coding: utf-8 -*-
#初始化所需参数:
#默认窗口大小
# 2022/2/26 修改了data_obtain 修复第一行数据无法利用问题


from typing import Tuple
from unicodedata import name
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from numpy import ndarray
from pandas import array
from utils import global_value
import numpy as np


def window_size() -> Tuple:

    """窗口参数 返回工作区 (width, height, title_height) """

    desktop = QApplication.desktop()
    screenRect = desktop.availableGeometry()
    screenheight = screenRect.height()
    screenwidth = screenRect.width()

    return screenwidth, screenheight
        
   
def ratio_size() -> float:

    """窗口比例 返回比例值: float"""
    
    ratio = window_size()[0]/960
    return ratio

def data_obtain() -> ndarray:
    """获取表格数据"""

    immediate_num = global_value.get_value('page_dict_1')['immediate_sheet'] #当前所在表格
    immediate_tablewidget = global_value.get_value('page_dict_1')['table_dict_' + str(immediate_num)]['Sheet'].tableWidget
    indexes = immediate_tablewidget.selectedIndexes() # 获取表格对象中被选中的数据索引列表
    indexes_dict = {}    
    for index in indexes: # 遍历每个单元格
        row, column = index.row(), index.column() # 获取单元格的行号，列号    
        if row in indexes_dict.keys():
            indexes_dict[row].append(column)
        else:
            indexes_dict[row] = [column]
    row_num = 0
    col_num = 0

    for i in indexes_dict.keys():
        row_num += 1
    
    #当数据列表第一项位于第一行时, 键值访问会出错, 因此区分位于第一行与第N行的情况

    dict_keys = [i for i in indexes_dict.keys()]

    if dict_keys[0] == 0:
        for j in range(len(indexes_dict[0])):      
            col_num += 1
    else:
        for j in range(len(indexes_dict[row_num])):   
            col_num += 1


    for row, columns in indexes_dict.items(): #去除多余空格     

        try:
            for column in columns:    
                redundant_data = float(immediate_tablewidget.item(row, column).text())
        except:
            row_num -= 1 

    data_array = np.zeros([row_num, col_num])
    

    row_current = 0
    for row, columns in indexes_dict.items():
        col_current = 0
        try:
            for column in columns:

                data = float(immediate_tablewidget.item(row, column).text())
                data_array[row_current][col_current] = data
                col_current += 1
            row_current += 1
        except:
            pass    

    return data_array


def data_normalize(data, scale = 100):
    """标准化数据"""
    new_data =[]
    for i in data:
        if np.sum(i) == scale:
            new_data.append(i)
        else:
            new_data.append((scale * i[0] / np.sum(i), scale * i[1] / np.sum(i), scale * i[2] / np.sum(i)))

    return new_data

def copy_text(tableWidget):
    """复制数据"""

    try:
        indexes = tableWidget.selectedIndexes() # 获取表格对象中被选中的数据索引列表
        indexes_dict = {}
        for index in indexes: # 遍历每个单元格
            row, column = index.row(), index.column() # 获取单元格的行号，列号
            
            if row in indexes_dict.keys():
                indexes_dict[row].append(column)
            else:
                indexes_dict[row] = [column]

    # 将数据表数据用制表符(\t)和换行符(\n)连接，使其可以复制到excel文件中



        text = ''
        for row, columns in indexes_dict.items():
            row_data = ''
            for column in columns:
                try:
                    data = tableWidget.item(row, column).text()
                except:
                    data = ' '
                if row_data:
                    row_data = row_data + '\t' + data
                else:
                    row_data = data
            if text:
                text = text + '\n' + row_data
            else:
                text = row_data
        return text + '\n'

    except BaseException as e:
        print('BaseException')
        return ''