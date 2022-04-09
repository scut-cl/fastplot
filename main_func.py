# 2022/2/20 复制到剪贴板功能在选中无数据单元格时，粘贴后出现问题(已解决)
# 2022/2/20 重新定义了全局变量字典 dict_keys(['app_path', 'page_count', 'immediate_page_num', 'page_dict_1'])
# 2022/2/20 'page_dict_1' dict_keys(['tab_number', 'page_num', 'immediate_sheet', 'table_dict_1', 'table_dict_2', 'table_dict_3'])

import sys, time, pyperclip, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from matplotlib.pyplot import table
from main_framework import Main_window
from utils.utils import window_size
from PyQt5 import QtWidgets, QtCore
from utils import global_value
from utils.utils import copy_text



def set_global():
    """ 定义跨模块全局变量 """

    # 全局参数变量
    app_path = os.path.dirname(os.path.abspath(__file__))
    print(app_path)
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
        
        self.app_path = global_value.get_value('app_path').replace('\\','/')
        self.setupUi(self, title_height) 
        self.resize(window_size()[0] * 0.5, window_size()[1] * 0.5)
        self.setWindowTitle('Fastplot')
        self.setWindowIcon(QIcon(self.app_path + "/graph/fastplot.png"))
        
    def keyPressEvent(self, event):

        super().keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_C and (event.modifiers() & QtCore.Qt.ControlModifier):
            #print('push C')

            try:

                immediate_num = global_value.get_value('page_dict_1')['immediate_sheet'] #当前所在表格
                immediate_tablewidget = global_value.get_value('page_dict_1')['table_dict_' + str(immediate_num)]['Sheet'].tableWidget
                text = copy_text(immediate_tablewidget) # 获取当前表格选中的数据tableWidget
                #print('text:', text)
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
              

                #print(text_data)
                for row in range(data_row_num):
                    for col in range(data_column_num):
                        position = row * data_column_num + col
                        immediate_tablewidget.setItem(row + r, col + c, QTableWidgetItem(text_data[position]))
            except:
                print('数据错误')

class Title_detect():

    def __init__(self) -> None:

        self.app_path = global_value.get_value('app_path').replace('\\','/')        
        self.widget = QWidget()
        self.widget.resize(316, 202)
        self.widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setWindowTitle(' ')
        self.widget.setWindowIcon(QIcon(self.app_path + "/graph/blank.png"))

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 10, 181, 131))
        self.label.setStyleSheet("border-image: url(" + self.app_path + "/graph/fastplot_label.png);")        
        self.text_label = QtWidgets.QLabel(self.widget)
        self.text_label.setGeometry(QtCore.QRect(100, 155, 121, 21))
        self.text_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.text_label.setText('Fastplot version1.0')
        self.widget.show()


        self.title_height = None
        self.title_measure()   

        self.timer = QTimer(self.widget)
        self.timer.timeout.connect(self.widget.close)
        self.timer.start(2000)                 #设定2秒后关闭初始化窗口


    def title_measure(self):

        self.title_height = self.widget.frameGeometry().height() - self.widget.geometry().height()



if __name__ == '__main__':
    
    set_global()  # 设置跨模块全局变量    

    #测量任务栏高度
    app_appearance = QApplication(sys.argv)

    title_detect = Title_detect()

    title_height = title_detect.title_height
    
    app_appearance.exec_()

    app = QApplication(sys.argv)
    
    myWin = MyMainWindow(title_height= title_height)
    myWin.show()
    sys.exit(app.exec_())
    