#2022/2/22 设置标签页文档模式
#2022/2/23 重新设置tab选项卡栏


from utils.utils import ratio_size, window_size
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget
from utils import global_value
from table_element import table_element


class Ui_table_module(object):
    """表格模块界面"""

    def setupUi(self, table_module):
        table_module.setObjectName("table_module")
        #table_module.resize(960 * self.ratio_size, 387 * self.ratio_size)
        table_module.setStyleSheet("background-color: rgb(230, 230, 230);") #!!!!!!背景颜色
        
        #页面栏
        self.sheet_bar = QtWidgets.QLabel(table_module)
        self.sheet_bar.setGeometry(QtCore.QRect(0 * self.ratio_size, 
                                                self.height_bias -  16 * self.ratio_size, 
                                                960 * self.ratio_size, 
                                                16 * self.ratio_size))
        self.sheet_bar.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.sheet_bar.setObjectName("sheet_bar")
        
        #tabwidget
        self.tabWidget_sheet = QtWidgets.QTabWidget(table_module)
        self.tabWidget_sheet.setGeometry(QtCore.QRect(0 * self.ratio_size, 
                                                      94 * self.ratio_size, 
                                                      960 * self.ratio_size, 
                                                      self.widget_height))
        font = QtGui.QFont()
        font.setPointSize(7 * self.ratio_size)
        self.tabWidget_sheet.setFont(font)
        self.tabWidget_sheet.setStyleSheet("QTabBar::tab{"\
                                                          "max-width:" + str(52 * self.ratio_size) +"; min-width:" + str(52 * self.ratio_size) +"; min-height:"+ str(16 * self.ratio_size) +";"\
                                                         " font:" + str(9 * self.ratio_size) +";\
                                                          padding: 0px;\
                                                        }\
                            QTabBar::tab:first:selected {\
                                                         margin-left: 30; margin-right: 0;\
                                                         color: black;\
                                                         border-image: url(" + self.app_path + "/graph/Sheet_select_0.png);\
                                                        }\
                            QTabBar::tab:first:!selected {\
                                                         color: black;\
                                                         margin-left: 30; margin-right: 0;\
                                                         border-image: url(" + self.app_path + "/graph/Sheet_hiden_0.png);\
                                                         }\
                            QTabBar::tab:middle:selected {\
                                                         margin-top: 0; margin-left: 0; margin-right: 0;\
                                                         color: black;\
                                                         border-image: url(" + self.app_path + "/graph/Sheet_select_1.png);\
                                                         }\
                            QTabBar::tab:middle:!selected {\
                                                         color: black;\
                                                         margin-top: 0; margin-left: 0; margin-right: 0;\
                                                         border-image: url(" + self.app_path + "/graph/Sheet_hiden_1.png);\
                                                         }\
                            QTabBar::tab:last:selected {\
                                                         margin-top: 0px; margin-left: 0; margin-right: 0;\
                                                         color: black;\
                                                         border-image: url(" + self.app_path + "/graph/Sheet_select_1.png);\
                                                       }\
                            QTabBar::tab:last:!selected {\
                                                         color: black;\
                                                         margin-top: 0; margin-left: 0; margin-right: 0;\
                                                         border-image: url(" + self.app_path + "/graph/Sheet_hiden_1.png);\
                                                        }\
                                                       ")

        self.tabWidget_sheet.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_sheet.setObjectName("tabWidget_sheet")
        self.tabWidget_sheet.setCurrentIndex(0)
        self.tabWidget_sheet.setDocumentMode(True)           #文档模式
        #self.tabWidget_sheet.setTabsClosable(True)          #关闭按钮        

        #增加页面
        self.pushButton_add_sheet = QtWidgets.QPushButton(table_module)
        self.pushButton_add_sheet.setGeometry(QtCore.QRect(520 * self.ratio_size, 
                                                           self.height_bias - 14 * self.ratio_size, 
                                                           13 * self.ratio_size, 
                                                           13 * self.ratio_size))

        self.pushButton_add_sheet.setStyleSheet("border-image: url(" + self.app_path + "/graph/add_sheet.png);"
                                                "background-color: rgba(230, 230, 230, 0);")
        self.pushButton_add_sheet.setObjectName("pushButton_add_sheet")
        
        #水平滚动条
        self.horizontalScrollBar = QtWidgets.QScrollBar(table_module)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(583 * self.ratio_size, 
                                                          self.height_bias - 15 * self.ratio_size, 
                                                          363 * self.ratio_size, 
                                                          14 * self.ratio_size))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")    


        
class table_module(QWidget, Ui_table_module):
    """表格模块"""

    def __init__(self, file_modle, title_height):
        super().__init__()
        
        self.init_ui(file_modle, title_height) # 实例化窗体



    def init_ui(self, file_modle, title_height):
        
        self.app_path = global_value.get_value('app_path').replace('\\','/')
        self.file_modle = file_modle
        self.title_height = title_height

        self.ratio_size =  ratio_size()
        self.height_bias = self.height_bias(title_height)
        self.widget_height = self.widget_height(title_height)   
        
        self.setupUi(file_modle)                  # 实例化控件

        self._init_table()
        self.widget_action()
        

    
    def _init_table(self):
        """页面初始化两个表格"""
        
        for i in range(2):
            self.add_tab()


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
        """控件事件"""
        self.pushButton_add_sheet.clicked.connect(self.add_tab)

        self.tabWidget_sheet.currentChanged.connect(self.tabchange)
        #self.pushButton_show.clicked.connect(self.page_show)
        
 
    def tabchange(self):
        '''切换标签页时更新滚动条的值'''

        current_tab_num = self.tabWidget_sheet.currentIndex() + 1 #按下的标签页
        global_value.get_value('page_dict_1')['immediate_sheet'] = current_tab_num

        table_dict = global_value.get_value('page_dict_1')['table_dict_' + str(current_tab_num)]
        Sheet = table_dict['Sheet']
        horizontalScrollBar = table_dict['horizontalScrollBar']
        col_value = Sheet.column_num
        slider_value = horizontalScrollBar.value()
        self.horizontalScrollBar.setMaximum(col_value - 16)
        self.horizontalScrollBar.setSliderPosition(slider_value)
        
                    
    def add_tab(self):
        """添加表格"""

        self.tab_num = global_value.get_value('page_dict_1')['tab_number']
        
        
        if self.tab_num <= 8:
            self.sheet = QtWidgets.QWidget()
            self.tabWidget_sheet.addTab(self.sheet, "Sheet" + str(self.tab_num + 1))
            #self.tabWidget_sheet.setTabsClosable(True)          #关闭按钮
            self.tab_num += 1

            table_dict = {}

            table_dict['self.sheet'] = self.sheet
            table_dict['horizontalScrollBar'] = self.horizontalScrollBar
            self.table_element_object = table_element(self.sheet, 
                                                    self.title_height, 
                                                    self.horizontalScrollBar)
            table_dict['Sheet'] = self.table_element_object

            global_value.get_value('page_dict_1')['table_dict_' + str(self.tab_num)] = table_dict
            global_value.get_value('page_dict_1')['tab_number'] = self.tab_num   #更新标签页数

        #print(global_value._global_dict['page_dict_1'].keys())

    def module_hide(self):
        """隐藏模块"""

        self.sheet_bar.hide()
        self.tabWidget_sheet.hide()
        self.pushButton_add_sheet.hide()
        self.horizontalScrollBar.hide()

    def module_show(self):
        """展示模块"""

        self.sheet_bar.show()
        self.tabWidget_sheet.show()
        self.pushButton_add_sheet.show()
        self.horizontalScrollBar.show()

    
