# 2022/2/20 复制到剪贴板功能在选中无数据单元格时，粘贴后出现问题
# 2022/2/20 重新定义了全局变量字典 dict_keys(['app_path', 'page_count', 'immediate_page_num', 'page_dict_1'])
# 2022/2/20 'page_dict_1' dict_keys(['tab_number', 'page_num', 'immediate_sheet', 'table_dict_1', 'table_dict_2', 'table_dict_3'])

import sys, time, pyperclip, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from matplotlib.pyplot import table
from main_framework import Main_window
from utils.utils import window_size
from PyQt5 import QtWidgets, QtCore
from utils import global_value

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


def set_global():
    """ 定义跨模块全局变量 """

    # 全局参数变量
    app_path = os.path.dirname(os.path.abspath(__file__))
    print('app_path', app_path)
    global_value.set_value('app_path', app_path)
    #global_value.set_value('tab_number', 0) #初始化标签页数
    #global_value.set_value('immediate_sheet', 1) #显示的表格页面
    global_value.set_value('page_count', 1) #页面选项卡数目
    global_value.set_value('immediate_page_num', 1) #初始时显示第一页(数据表格页)
    page_dict = {'tab_number': 0, 'page_num': 1, 'immediate_sheet': 1}        #初始化标签页数, 页面位置, 显示的表格页面
    global_value.set_value('page_dict_1', page_dict) #初始化页面内容(数据表格页)
    

global_value._init()

class MyMainWindow(QMainWindow, Main_window):

    def __init__(self, title_height) -> None:
        super(MyMainWindow, self).__init__( )
        
        self.setupUi(self, title_height) 
        self.resize(window_size()[0] * 0.5, window_size()[1] * 0.5)

    def keyPressEvent(self, event):

        super().keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_C and (event.modifiers() & QtCore.Qt.ControlModifier):

            try:

                immediate_num = global_value.get_value('page_dict_1')['immediate_sheet'] #当前所在表格
                immediate_tablewidget = global_value.get_value('page_dict_1')['table_dict_' + str(immediate_num)]['Sheet'].tableWidget
                text = copy_text(immediate_tablewidget) # 获取当前表格选中的数据tableWidget

                if text:
                    pyperclip.copy(text) # 复制数据到粘贴板            

            except:
                print('无数据')


        elif event.key() == QtCore.Qt.Key_V and (event.modifiers() & QtCore.Qt.ControlModifier):
            
            try:
                clipboard = QApplication.clipboard()
                text = clipboard.text()

                text_data = text.replace('\n', ',').replace('\t', ',').split(',')
                data_row_num = text.count('\n') 
                data_column_num = int(text.count('\t')/data_row_num) + 1

                immediate_num = global_value.get_value('page_dict_1')['immediate_sheet']     #当前所在表格
                immediate_tableobject = global_value.get_value('page_dict_1')['table_dict_' + str(immediate_num)]['Sheet']       
                immediate_tablewidget = immediate_tableobject.tableWidget

                r = immediate_tablewidget.currentRow() 
                c = immediate_tablewidget.currentColumn() 
            
                if r + data_row_num > immediate_tableobject.row_num:
                    immediate_tableobject.row_num = r + data_row_num 
                    immediate_tablewidget.setRowCount(immediate_tableobject.row_num)
              

                for row in range(data_row_num):
                    for col in range(data_column_num):
                        position = row * data_column_num + col
                        immediate_tablewidget.setItem(row + r, col + c, QTableWidgetItem(text_data[position]))
            except:
                print('数据错误')

class title_detect(object):

    def __init__(self) -> None:
        self.title_height = None

    def create_window(self):
        app = QtWidgets.QApplication(sys.argv)

        window = QtWidgets.QWidget()

        #window.setWindowTitle("在屏幕中央显示窗口")

        window.resize(200, 200)

        window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        window.show()

        self.title_height = window.frameGeometry().height() - window.geometry().height()

        time.sleep(1)

        window.close()




if __name__ == '__main__':
    
    #测量任务栏高度
    title_detect = title_detect()
    title_detect.create_window()
    title_height = title_detect.title_height
    


    set_global()  # 设置跨模块全局变量

    app = QApplication(sys.argv)
    
    myWin = MyMainWindow(title_height= title_height)
    myWin.show()
    sys.exit(app.exec_())
    