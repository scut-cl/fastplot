# -*- coding: utf-8 -*-
#初始化所需参数:
#默认窗口大小

# -*- coding: utf-8 -*-
#初始化所需参数:
#默认窗口大小

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
    
    for j in range(len(indexes_dict[row_num])):
        col_num += 1

    data_array = np.zeros([row_num, col_num])

    row_current = 0
    for row, columns in indexes_dict.items():
        col_current = 0
        for column in columns:
            try:
                data = float(immediate_tablewidget.item(row, column).text())
            except:
                data = 0    
            data_array[row_current][col_current] = data
            col_current += 1

        row_current += 1

    return data_array

