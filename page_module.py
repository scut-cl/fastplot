# 2022/2/23 更新全局列表, 新增页面对象'page_object' dict_keys(['app_path', 'page_count', 'immediate_page_num', 'page_dict_1', 'page_object'])

from utils.utils import ratio_size, window_size
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QVBoxLayout
from utils import global_value
from table_module import table_module
from image_dialog import image_dialog
from processing_dialog import Single_dialog


class Ui_page_module(object):
    """页面选项卡模块界面"""

    def setupUi(self, main_window):

        main_window.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:10, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(230, 230, 230, 255));\n") #!!!!!!背景颜色   
        
        #tabwidget
        self.tabWidget_page = QtWidgets.QTabWidget(main_window)
        self.tabWidget_page.setGeometry(QtCore.QRect(0 * self.ratio_size, 
                                                      78 * self.ratio_size, 
                                                      960 * self.ratio_size, 
                                                      self.widget_height))
        font = QtGui.QFont()
        font.setPointSize(7 * self.ratio_size)
        self.tabWidget_page.setFont(font)
        
        self.tabWidget_page.setStyleSheet("QTabBar::tab{"\
                                                          "max-width:" + str(92 * self.ratio_size) +"; min-width:" + str(92 * self.ratio_size) +"; min-height:"+ str(16 * self.ratio_size) +";"\
                                                         " font:" + str(7 * self.ratio_size) +";\
                                                          padding: 0px;\
                                                          border-image: url(" + self.app_path + "/graph/page_select.png);\
                                                        }\
                            QTabBar::tab:first:selected {\
                                                         margin-left: 0; margin-right: 0;\
                                                         color: black;\
                                                         border-image: url(" + self.app_path + "/graph/page_select.png);\
                                                        }\
                            QTabBar::tab:first:!selected {\
                                                         color: black;\
                                                         margin-left: 0; margin-right: 0;\
                                                         border-image: url(" + self.app_path + "/graph/page_hiden.png);\
                                                         }\
                            QTabBar::tab:middle:selected {\
                                                         margin-top: 0; margin-left: 0; margin-right: 0;\
                                                         color: black;\
                                                         border-image: url(" + self.app_path + "/graph/page_select.png);\
                                                         }\
                            QTabBar::tab:middle:!selected {\
                                                         color: black;\
                                                         margin-top: 0; margin-left: 0; margin-right: 0;\
                                                         border-image: url(" + self.app_path + "/graph/page_hiden.png);\
                                                         }\
                            QTabBar::tab:last:selected {\
                                                         margin-top: 0px; margin-left: 0; margin-right: 0;\
                                                         color: black;\
                                                         border-image: url(" + self.app_path + "/graph/page_select.png);\
                                                       }\
                            QTabBar::tab:last:!selected {\
                                                         color: black;\
                                                         margin-top: 0; margin-left: 0; margin-right: 0;\
                                                         border-image: url(" + self.app_path + "/graph/page_hiden.png);\
                                                        }\
                                                 QTabBar{background-color: qlineargradient(spread:pad, x1:0, y1:10, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(230, 230, 230, 255))};\
                                                        ")
        
        self.tabWidget_page.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_page.setObjectName("tabWidget_page")
        self.tabWidget_page.setCurrentIndex(0)
        self.tabWidget_page.setDocumentMode(True) 
        self.tabWidget_page.setTabsClosable(True)        


class page_block_module(QWidget, Ui_page_module):
    """页面模块逻辑"""

    def __init__(self, main_window, title_height) -> None:
        super().__init__()
        
        self.app_path = global_value.get_value('app_path').replace('\\','/')
        self.ratio_size =  ratio_size()
        self.widget_height = self.widget_height(title_height)
        self.setupUi(main_window)
        self._init_()
        self.add_table(main_window, title_height)
    
        self.widget_action()

    def _init_(self):
        """建立一个页表"""

        global_value.set_value('page_object', self.tabWidget_page)
    
    def add_table(self, main_window, title_height):
        """建立表格页"""

        tabwidget = global_value.get_value('page_object')
        self.table_widget = table_module(main_window, title_height)
        tabwidget.addTab(self.table_widget, "数据表格")        

        
    def height_bias(self, title_height) -> float:
        """竖直位置参数修正"""

        bias = window_size()[1] - 0.75 * title_height - 11 * self.ratio_size

        return bias
    
    def widget_height(self, title_height) -> float:
        """控件高度修正"""

        bias = window_size()[1] - 0.75 * title_height - 11 * self.ratio_size \
               - 78 * self.ratio_size

        return bias        
    


    def widget_action(self):
        """控件事件"""

        self.tabWidget_page.currentChanged.connect(self.tab_change)
        self.tabWidget_page.tabCloseRequested.connect(self.tab_close)

    
    def tab_change(self):
        """改变标签页"""

        if self.tabWidget_page.currentIndex() + 1 == 1:
            self.table_widget.module_show()
        
        else:
            self.table_widget.module_hide()

    def tab_close(self, currentIndex):
        """关闭选项卡或清除表格数据"""
        
        if currentIndex == 0:
            tab_num = global_value.get_value('page_dict_1')['tab_number']
            for i in range(tab_num):
                
                self.table_widget.tabWidget_sheet.removeTab(tab_num - i)
            
            global_value.get_value('page_dict_1')['tab_number'] = 1
            self.table_widget.add_tab()
        
        else:
            self.tabWidget_page.removeTab(currentIndex)



class image_tab(QWidget):
    """创建一个绘图页面"""

    def __init__(self, widget_height) -> None:
        super(image_tab, self).__init__()

        self.image_dialog = image_dialog()
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0 , 960 * ratio_size(), widget_height))  

        self.layout = QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)


class processing_tab(QWidget):
    """创建一个拟合页面"""

    def __init__(self, widget_height) -> None:
        super(processing_tab, self).__init__()       

        self.single_dialog = Single_dialog()
        self.image_dialog = image_dialog()
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0 , 960 * ratio_size(), widget_height))  

        self.layout = QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
