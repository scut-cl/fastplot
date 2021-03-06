
from utils.utils import ratio_size, window_size, data_obtain
from PyQt5 import QtCore, QtGui, QtWidgets
from MatplotlibWidget import (Scatter_graph, 
                              Solidline_graph, 
                              Bar_graph, 
                              Step_graph,
                              Stem_graph,
                              Threedimension_graph,
                              Error_graph,
                              Histogram3D_graph,
                              Ternary_graph,
                              )
from utils import global_value
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from page_module import image_tab

class Ui_image_pattern_module(object):
    """图像样式模块"""


    def setupUi(self, image_pattern_module):
        """图像样式模块UI"""

        image_pattern_module.setObjectName("image_pattern_module")
        image_pattern_module.resize(509 * self.ratio_size, 49 * self.ratio_size)

        #模块分割线
        self.line = QtWidgets.QFrame(image_pattern_module)
        self.line.setGeometry(QtCore.QRect(507 * self.ratio_size, 0 * self.ratio_size + self.height_bias, 5 * self.ratio_size, 48 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setBold(True)
        font.setWeight(75 * self.ratio_size)
        self.line.setFont(font)
        self.line.setStyleSheet("background-color: rgba(247, 240, 240, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        #散点图
        self.pushButton_Scatter = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_Scatter.setGeometry(QtCore.QRect(17 * self.ratio_size, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_Scatter.setStyleSheet("border-image: url(" + self.app_path + "/graph/Scatter.png);\n"
                                              "background-color: rgba(247, 240, 240, 0);")
        self.pushButton_Scatter.setText("")
        self.pushButton_Scatter.setObjectName("pushButton_Scatter")

        self.label_Scatter = QtWidgets.QLabel(image_pattern_module)
        self.label_Scatter.setGeometry(QtCore.QRect(17 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_Scatter.setFont(font)
        self.label_Scatter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Scatter.setObjectName("label_Scatter")
        self.label_Scatter.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        #实线图
        self.label_solidline = QtWidgets.QLabel(image_pattern_module)
        self.label_solidline.setGeometry(QtCore.QRect(74 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_solidline.setFont(font)
        self.label_solidline.setAlignment(QtCore.Qt.AlignCenter)
        self.label_solidline.setObjectName("label_solidline")
        self.label_solidline.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        self.pushButton_solidline = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_solidline.setGeometry(QtCore.QRect(74 * self.ratio_size, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_solidline.setStyleSheet("border-image: url(" + self.app_path + "/graph/solidline.png);\n"
                                                "background-color: rgba(247, 240, 240, 0);")
        self.pushButton_solidline.setText("")
        self.pushButton_solidline.setObjectName("pushButton_solidline")

        #柱状图
        self.pushButton_Histogram = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_Histogram.setGeometry(QtCore.QRect(130 * self.ratio_size, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_Histogram.setStyleSheet("border-image: url(" + self.app_path + "/graph/Histogram.png);\n"
                                                "background-color: rgba(247, 240, 240, 0);")
        self.pushButton_Histogram.setText("")
        self.pushButton_Histogram.setObjectName("pushButton_Histogram")

        self.label_Histogram = QtWidgets.QLabel(image_pattern_module)
        self.label_Histogram.setGeometry(QtCore.QRect(130 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_Histogram.setFont(font)
        self.label_Histogram.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Histogram.setObjectName("label_Histogram")
        self.label_Histogram.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        #阶梯图
        self.pushButton_Stairs = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_Stairs.setGeometry(QtCore.QRect(187 * self.ratio_size, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_Stairs.setStyleSheet("border-image: url(" + self.app_path + "/graph/Stairs.png);\n"
                                             "background-color: rgba(247, 240, 240, 0);")
        self.pushButton_Stairs.setText("")
        self.pushButton_Stairs.setObjectName("pushButton_Stairs")

        self.label_Stairs = QtWidgets.QLabel(image_pattern_module)
        self.label_Stairs.setGeometry(QtCore.QRect(187 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_Stairs.setFont(font)
        self.label_Stairs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Stairs.setObjectName("label_Stairs")
        self.label_Stairs.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        #垂线图
        self.pushButton_vertical_line = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_vertical_line.setGeometry(QtCore.QRect(244 * self.ratio_size, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_vertical_line.setStyleSheet("border-image: url(" + self.app_path + "/graph/vertical_line.png);\n"
                                                    "background-color: rgba(247, 240, 240, 0);")
        self.pushButton_vertical_line.setText("")
        self.pushButton_vertical_line.setObjectName("pushButton_vertical_line")

        self.label_vertical_line = QtWidgets.QLabel(image_pattern_module)
        self.label_vertical_line.setGeometry(QtCore.QRect(244 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_vertical_line.setFont(font)
        self.label_vertical_line.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vertical_line.setObjectName("label_vertical_line")
        self.label_vertical_line.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        #三维图
        self.pushButton_three_dimensional = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_three_dimensional.setGeometry(QtCore.QRect(299 * self.ratio_size, 0 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 31 * self.ratio_size))
        self.pushButton_three_dimensional.setStyleSheet("border-image: url(" + self.app_path + "/graph/three-dimensional.png);\n"
                                                        "background-color: rgba(247, 240, 240, 0);")
        self.pushButton_three_dimensional.setText("")
        self.pushButton_three_dimensional.setObjectName("pushButton_three_dimensional")

        self.label_three_dimensional = QtWidgets.QLabel(image_pattern_module)
        self.label_three_dimensional.setGeometry(QtCore.QRect(299 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_three_dimensional.setFont(font)
        self.label_three_dimensional.setAlignment(QtCore.Qt.AlignCenter)
        self.label_three_dimensional.setObjectName("label_three_dimensional")
        self.label_three_dimensional.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        #三维柱状图
        self.pushButton_Histogram_3D = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_Histogram_3D.setGeometry(QtCore.QRect(410 * self.ratio_size, 0 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 31 * self.ratio_size))
        self.pushButton_Histogram_3D.setStyleSheet("border-image: url(" + self.app_path + "/graph/Histogram_3D.png);\n"
                                                   "background-color: rgba(255, 255, 255, 0);")
        self.pushButton_Histogram_3D.setText("")
        self.pushButton_Histogram_3D.setObjectName("pushButton_Histogram_3D")

        self.label_Histogram_3D = QtWidgets.QLabel(image_pattern_module)
        self.label_Histogram_3D.setGeometry(QtCore.QRect(410 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_Histogram_3D.setFont(font)
        self.label_Histogram_3D.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Histogram_3D.setObjectName("label_Histogram_3D")
        self.label_Histogram_3D.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        #误差图
        self.label_error = QtWidgets.QLabel(image_pattern_module)
        self.label_error.setGeometry(QtCore.QRect(356 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_error.setFont(font)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.label_error.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        self.pushButton_error = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_error.setGeometry(QtCore.QRect(356 * self.ratio_size, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_error.setStyleSheet("border-image: url(" + self.app_path + "/graph/error.png);\n"
                                            "background-color: rgba(255, 255, 255, 0);")
        self.pushButton_error.setText("")
        self.pushButton_error.setObjectName("pushButton_error")

        #三角图
        self.label_triangle = QtWidgets.QLabel(image_pattern_module)
        self.label_triangle.setGeometry(QtCore.QRect(465 * self.ratio_size, 30 * self.ratio_size + self.height_bias, 31 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_triangle.setFont(font)
        self.label_triangle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_triangle.setObjectName("label_triangle")
        self.label_triangle.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        self.pushButton_triangle = QtWidgets.QPushButton(image_pattern_module)
        self.pushButton_triangle.setGeometry(QtCore.QRect(465 * self.ratio_size, 1 * self.ratio_size + self.height_bias, 31 * self.ratio_size, 27 * self.ratio_size))
        self.pushButton_triangle.setStyleSheet("border-image: url(" + self.app_path + "/graph/triangle.png);\n"
                                               "background-color: rgba(255, 255, 255, 0);")
        self.pushButton_triangle.setText("")
        self.pushButton_triangle.setObjectName("pushButton_triangle")

        #模块名称
        self.name_image_parttern = QtWidgets.QLabel(image_pattern_module)
        self.name_image_parttern.setGeometry(QtCore.QRect(238 * self.ratio_size, 38 * self.ratio_size + self.height_bias, 34 * self.ratio_size, 12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(6 * self.ratio_size)
        font.setBold(True)
        font.setWeight(75)
        self.name_image_parttern.setFont(font)
        self.name_image_parttern.setStyleSheet("background-color: rgba(247, 240, 240, 0);")
        self.name_image_parttern.setObjectName("name_image_parttern")

        self.retranslateUi(image_pattern_module)
        QtCore.QMetaObject.connectSlotsByName(image_pattern_module)

    def retranslateUi(self, image_pattern_module):
        _translate = QtCore.QCoreApplication.translate
        image_pattern_module.setWindowTitle(_translate("image_pattern_module", "Form"))
        self.label_Scatter.setText(_translate("image_pattern_module", "散点"))
        self.label_solidline.setText(_translate("image_pattern_module", "实线"))
        self.label_Histogram.setText(_translate("image_pattern_module", "柱状"))
        self.label_Stairs.setText(_translate("image_pattern_module", "阶梯"))
        self.label_vertical_line.setText(_translate("image_pattern_module", "垂线"))
        self.label_three_dimensional.setText(_translate("image_pattern_module", "三维"))
        self.label_Histogram_3D.setText(_translate("image_pattern_module", "三维柱状"))
        self.label_error.setText(_translate("image_pattern_module", "误差线"))
        self.label_triangle.setText(_translate("image_pattern_module", "三角"))
        self.name_image_parttern.setText(_translate("image_pattern_module", "图像样式"))

class image_pattern_module(Ui_image_pattern_module):
    
    def __init__(self, main_window, title_height) -> None:

        self.height_bias = self.height_bias()
        self.main_window = main_window
        self.title_height = title_height
        self.ratio_size = ratio_size()
        self.widget_height = self.widget_height(title_height)
        self.app_path = global_value.get_value('app_path').replace('\\','/')
        self.ratio_size =  ratio_size()
        self.setupUi(main_window) 

        self.widget_action()

    def height_bias(self) -> float:
        """竖直位置参数修正"""
        bias = 26.5 * ratio_size()
        return bias


    def widget_height(self, title_height) -> float:
        """控件高度修正"""

        bias = window_size()[1] - 0.75 * title_height - 11 * self.ratio_size \
               - 94 * self.ratio_size

        return bias   


    def paint_Scatter(self):
        """绘制散点图"""

        tab = image_tab(self.widget_height)    
        self.Scatter_graph = Scatter_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)
        self.Scatter_Toolbar = NavigationToolbar(self.Scatter_graph, tab.verticalLayoutWidget)  
        tab.layout.addWidget(self.Scatter_graph)
        tab.layout.addWidget(self.Scatter_Toolbar)
        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '散点图') 

        self.Scatter_graph.plot_function()
        
        
    
    def paint_Soildline(self):
        """绘制实线图"""

        tab = image_tab(self.widget_height)                                                                 #创建绘图页面
        #paint_params = tab.image_dialog.apply_params()                                                      #调用绘图方法
        self.Solidline_graph = Solidline_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        self.Solidline_Toolbar = NavigationToolbar(self.Solidline_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(self.Solidline_graph)
        tab.layout.addWidget(self.Solidline_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '实线图')

        self.Solidline_graph.plot_function()

    def paint_bar(self):
        """绘制柱状图"""        

        tab = image_tab(self.widget_height)
        bar_graph = Bar_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        bar_Toolbar = NavigationToolbar(bar_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(bar_graph)
        tab.layout.addWidget(bar_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '柱状图')

        bar_graph.plot_function()        
        
          
    def paint_step(self):
        """绘制阶梯图"""

        tab = image_tab(self.widget_height)
        step_graph = Step_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        step_Toolbar = NavigationToolbar(step_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(step_graph)
        tab.layout.addWidget(step_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '阶梯图')

        step_graph.plot_function()        

    def paint_vertical(self):
        """绘制垂线图"""

        tab = image_tab(self.widget_height)
        stem_graph = Stem_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        step_Toolbar = NavigationToolbar(stem_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(stem_graph)
        tab.layout.addWidget(step_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '垂线图')

        stem_graph.plot_function()        

    def paint_3D(self):
        """三维图"""

        tab = image_tab(self.widget_height)
        threedimension_graph = Threedimension_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        step_Toolbar = NavigationToolbar(threedimension_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(threedimension_graph)
        tab.layout.addWidget(step_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '三维图')

        threedimension_graph.plot_function()              
    
    def error_bar(self):
        """误差图"""

        tab = image_tab(self.widget_height)
        error_graph = Error_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        step_Toolbar = NavigationToolbar(error_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(error_graph)
        tab.layout.addWidget(step_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '误差图')

        error_graph.plot_function()         

    def bar_3d(self):
        """三维柱状"""

        tab = image_tab(self.widget_height)
        histogram3D_graph = Histogram3D_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        step_Toolbar = NavigationToolbar(histogram3D_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(histogram3D_graph)
        tab.layout.addWidget(step_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '三维柱状')

        histogram3D_graph.plot_function()         
    
    def ternary_graph(self):
        """三角图"""

        tab = image_tab(self.widget_height)
        ternary_graph = Ternary_graph(tab.image_dialog, tab.verticalLayoutWidget, width=5, height=2)   #绘制图像
        step_Toolbar = NavigationToolbar(ternary_graph, tab.verticalLayoutWidget)         
        tab.layout.addWidget(ternary_graph)
        tab.layout.addWidget(step_Toolbar)

        tabwidget = global_value.get_value('page_object')
        tabwidget.addTab(tab, '三角图')

        ternary_graph.plot_function()                
    




    def widget_action(self):
        '''控件事件'''
        
        self.pushButton_Scatter.clicked.connect(self.paint_Scatter)
        self.pushButton_solidline.clicked.connect(self.paint_Soildline)
        self.pushButton_Histogram.clicked.connect(self.paint_bar)
        self.pushButton_Stairs.clicked.connect(self.paint_step)
        self.pushButton_vertical_line.clicked.connect(self.paint_vertical)
        self.pushButton_three_dimensional.clicked.connect(self.paint_3D)
        self.pushButton_error.clicked.connect(self.error_bar)
        self.pushButton_Histogram_3D.clicked.connect(self.bar_3d)
        self.pushButton_triangle.clicked.connect(self.ternary_graph)

    def module_hide(self):
        """隐藏状态"""

        self.pushButton_Scatter.hide()
        self.label_Scatter.hide()
        self.pushButton_solidline.hide()
        self.label_solidline.hide()
        self.pushButton_Histogram.hide()
        self.label_Histogram.hide()
        self.pushButton_Stairs.hide()
        self.label_Stairs.hide()
        self.pushButton_vertical_line.hide()
        self.label_vertical_line.hide()
        self.pushButton_three_dimensional.hide()
        self.label_three_dimensional.hide()
        self.pushButton_Histogram_3D.hide()
        self.label_Histogram_3D.hide()
        self.pushButton_error.hide()
        self.label_error.hide()
        self.pushButton_triangle.hide()
        self.label_triangle.hide()
        self.name_image_parttern.hide()
        self.line.hide()

    def module_show(self):
        """显示状态"""

        self.pushButton_Scatter.show()
        self.label_Scatter.show()
        self.pushButton_solidline.show()
        self.label_solidline.show()
        self.pushButton_Histogram.show()
        self.label_Histogram.show()
        self.pushButton_Stairs.show()
        self.label_Stairs.show()
        self.pushButton_vertical_line.show()
        self.label_vertical_line.show()
        self.pushButton_three_dimensional.show()
        self.label_three_dimensional.show()
        self.pushButton_Histogram_3D.show()
        self.label_Histogram_3D.show()
        self.pushButton_error.show()
        self.label_error.show()
        self.pushButton_triangle.show()
        self.label_triangle.show()
        self.name_image_parttern.show()
        self.line.show()
