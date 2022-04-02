# 2022/2/22 设置文档模式后调整表格大小


from utils.utils import ratio_size, window_size
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget
from utils import global_value



class Ui_table_element(object):

    def table_element(self, sheet):

        self.tableWidget = QtWidgets.QTableWidget(sheet)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 960 * self.ratio_size, self.widget_height - 15 * self.ratio_size))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.row_num)                   #行数
        self.tableWidget.setColumnCount(self.column_num)             #列数
        
        for row_num in range(self.row_num):
            self.tableWidget.setRowHeight(row_num, 10 * self.ratio_size ) #行高
        for col_num in range(self.column_num):
            self.tableWidget.setColumnWidth(col_num, 57 * self.ratio_size) #列宽
        
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)#隐藏水平滚动条
        self.tableWidget.verticalScrollBar().setStyleSheet("background-color: rgb(230, 230, 230);")


class table_element(QWidget, Ui_table_element):
    
    def __init__(self, sheet, title_height, horizontalScrollBar):
        super().__init__()
        
        self.horizontalScrollBar = horizontalScrollBar
        self.init_ui(sheet, title_height) # 实例化窗体

        self.horizontalScrollBar.setMaximum(self.column_num - 16 * self.ratio_size) #初始化滚动条值


    def init_ui(self, sheet, title_height):

        self.ratio_size =  ratio_size()
        self.height_bias = self.height_bias(title_height)
        self.widget_height = self.widget_height(title_height)           

        self.row_num = int(30 * self.ratio_size)      #初始化表格行数
        self.column_num = int(30 * self.ratio_size)   #初始化表格列数
        self.ratio_size =  ratio_size()
       
        self.table_element(sheet) # 实例化控件
        self.widget_action()
        
    def height_bias(self, title_height) -> float:
        """竖直位置参数修正"""

        bias = window_size()[1] - 0.75 * title_height - 11 * self.ratio_size

        return bias
    
    def widget_height(self, title_height) -> float:
        """控件高度修正"""

        bias = window_size()[1] - 0.75 * title_height - 11 * self.ratio_size \
               - 94 * self.ratio_size

        return bias       

    def widget_action(self):
        
        self.tableWidget.verticalScrollBar().valueChanged.connect(self.row_change)
        self.tableWidget.horizontalScrollBar().valueChanged.connect(self.col_change)
        self.horizontalScrollBar.sliderMoved.connect(self.table_scroll_change)
    
    def row_change(self):
        """自动增加行数"""
        value = self.tableWidget.verticalScrollBar().value()
    
        if value >= (self.row_num - 16) and self.row_num <= 1048576:
            self.row_num += 16
            self.tableWidget.setRowCount(self.row_num)    
    
    def col_change(self):
        """1、自动增加列数,
           2、通过滚动条控制列位置"""
        value = self.tableWidget.horizontalScrollBar().value()

        self.horizontalScrollBar.setSliderPosition(value)        
    
        if value >= (self.column_num - 16 ) and self.column_num <= 1048576:
            self.column_num += 16
            self.tableWidget.setColumnCount(self.column_num)    
        
        self.horizontalScrollBar.setMaximum(self.column_num - 16)
    
    def table_scroll_change(self):
        
        value = self.horizontalScrollBar.value()
        self.tableWidget.horizontalScrollBar().setSliderPosition(value)

