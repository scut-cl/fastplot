# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\srp\fastplot\project\main_demo\code\ui\data_analysis_module.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from utils.utils import ratio_size
from PyQt5 import QtCore, QtGui, QtWidgets
from utils import global_value


class Ui_data_analysis_module(object):
    """分析模块"""

    def setupUi(self, data_analysis_module):
        """框架"""

        data_analysis_module.setObjectName("data_analysis_module")
        data_analysis_module.resize(184 * self.ratio_size, 49 * self.ratio_size)
        
        #单变量分析
        self.Univariate_img = QtWidgets.QLabel(data_analysis_module)
        self.Univariate_img.setGeometry(QtCore.QRect(14 * self.ratio_size + self.horizontal_bias, 
                                                     3 * self.ratio_size + self.height_bias, 
                                                     15 * self.ratio_size, 
                                                     16 * self.ratio_size))                                     
        self.Univariate_img.setStyleSheet("border-image: url(" + self.app_path + "/graph/Univariate.png);\n;"
                                          "background-color: rgb(247, 240, 240);")
        self.Univariate_img.setText("")
        self.Univariate_img.setObjectName("Univariate_img")

        self.Univariate_txt = QtWidgets.QLabel(data_analysis_module)
        self.Univariate_txt.setGeometry(QtCore.QRect(29 * self.ratio_size + self.horizontal_bias, 
                                                     3 * self.ratio_size + self.height_bias, 
                                                     43 * self.ratio_size, 
                                                     14 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.Univariate_txt.setFont(font)
        self.Univariate_txt.setObjectName("Univariate_txt")
        self.Univariate_txt.setStyleSheet("background-color: rgb(247, 240, 240);")
        
        self.pushButton_Univariate = QtWidgets.QPushButton(data_analysis_module)
        self.pushButton_Univariate.setGeometry(QtCore.QRect(14 * self.ratio_size + self.horizontal_bias, 
                                                            3 * self.ratio_size + self.height_bias, 
                                                            57 * self.ratio_size, 
                                                            17 * self.ratio_size))
        self.pushButton_Univariate.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_Univariate.setText("")
        self.pushButton_Univariate.setObjectName("pushButton_Univariate")
        
        #多变量分析
        self.Multivariable_img = QtWidgets.QLabel(data_analysis_module)
        self.Multivariable_img.setGeometry(QtCore.QRect(12 * self.ratio_size + self.horizontal_bias, 
                                                        21 * self.ratio_size + self.height_bias, 
                                                        17 * self.ratio_size, 
                                                        13 * self.ratio_size))
        self.Multivariable_img.setStyleSheet("border-image: url(" + self.app_path + "/graph/Multivariable.png);\n;"
                                             "background-color: rgb(247, 240, 240);")
        self.Multivariable_img.setText("")
        self.Multivariable_img.setObjectName("Multivariable_img")

        self.Multivariable_txt = QtWidgets.QLabel(data_analysis_module)
        self.Multivariable_txt.setGeometry(QtCore.QRect(28 * self.ratio_size + self.horizontal_bias, 
                                                        20 * self.ratio_size + self.height_bias, 
                                                        43 * self.ratio_size, 
                                                        14 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.Multivariable_txt.setFont(font)
        self.Multivariable_txt.setObjectName("Multivariable_txt")
        self.Multivariable_txt.setStyleSheet("background-color: rgb(247, 240, 240);")

        self.pushButton_Multivariable = QtWidgets.QPushButton(data_analysis_module)
        self.pushButton_Multivariable.setGeometry(QtCore.QRect(13 * self.ratio_size + self.horizontal_bias, 
                                                               19 * self.ratio_size + self.height_bias, 
                                                               57 * self.ratio_size, 
                                                               17 * self.ratio_size))
        self.pushButton_Multivariable.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_Multivariable.setText("")
        self.pushButton_Multivariable.setObjectName("pushButton_Multivariable")

        #波谱分析
        self.Spectral_analysis_img = QtWidgets.QLabel(data_analysis_module)
        self.Spectral_analysis_img.setGeometry(QtCore.QRect(108 * self.ratio_size + self.horizontal_bias, 
                                                            3 * self.ratio_size + self.height_bias, 
                                                            16 * self.ratio_size, 
                                                            16 * self.ratio_size))
        self.Spectral_analysis_img.setStyleSheet("border-image: url(" + self.app_path + "/graph/Spectral_analysis.png);\n;"
                                                 "background-color: rgb(247, 240, 240);")
        self.Spectral_analysis_img.setText("")
        self.Spectral_analysis_img.setObjectName("Spectral_analysis_img")

        self.Spectral_analysis_txt = QtWidgets.QLabel(data_analysis_module)
        self.Spectral_analysis_txt.setGeometry(QtCore.QRect(125 * self.ratio_size + self.horizontal_bias, 
                                                            3 * self.ratio_size + self.height_bias, 
                                                            43 * self.ratio_size, 
                                                            14 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.Spectral_analysis_txt.setFont(font)
        self.Spectral_analysis_txt.setObjectName("Spectral_analysis_txt")
        self.Spectral_analysis_txt.setStyleSheet("background-color: rgb(247, 240, 240);")

        self.pushButton_Spectral_analysis = QtWidgets.QPushButton(data_analysis_module)
        self.pushButton_Spectral_analysis.setGeometry(QtCore.QRect(103 * self.ratio_size + self.horizontal_bias, 
                                                                   2 * self.ratio_size + self.height_bias, 
                                                                   57 * self.ratio_size, 
                                                                   17 * self.ratio_size))
        self.pushButton_Spectral_analysis.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_Spectral_analysis.setText("")
        self.pushButton_Spectral_analysis.setObjectName("pushButton_Spectral_analysis")

        #模块分割线
        self.line = QtWidgets.QFrame(data_analysis_module)
        self.line.setGeometry(QtCore.QRect(182 * self.ratio_size + self.horizontal_bias, 
                                           0 * self.ratio_size + self.height_bias, 
                                           5 * self.ratio_size, 
                                           48 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setBold(True)
        font.setWeight(75 * self.ratio_size)
        self.line.setFont(font)
        self.line.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(data_analysis_module)
        self.line_2.setGeometry(QtCore.QRect(90 * self.ratio_size + self.horizontal_bias, 
                                             0 * self.ratio_size + self.height_bias, 
                                             5 * self.ratio_size, 
                                             36 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setBold(True)
        font.setWeight(75 * self.ratio_size)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #模块名称
        self.name_data_analysis = QtWidgets.QLabel(data_analysis_module)
        self.name_data_analysis.setGeometry(QtCore.QRect(75 * self.ratio_size + self.horizontal_bias, 
                                                         38 * self.ratio_size + self.height_bias, 
                                                         34 * self.ratio_size, 
                                                         12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(6 * self.ratio_size)
        font.setBold(True)
        font.setWeight(75 * self.ratio_size)
        self.name_data_analysis.setFont(font)
        self.name_data_analysis.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.name_data_analysis.setObjectName("name_data_analysis")

        self.retranslateUi(data_analysis_module)
        QtCore.QMetaObject.connectSlotsByName(data_analysis_module)

    def retranslateUi(self, data_analysis_module):
        _translate = QtCore.QCoreApplication.translate
        data_analysis_module.setWindowTitle(_translate("data_analysis_module", "Form"))
        self.Univariate_txt.setText(_translate("data_analysis_module", "单变量拟合"))
        self.Multivariable_txt.setText(_translate("data_analysis_module", "多变量拟合"))
        self.Spectral_analysis_txt.setText(_translate("data_analysis_module", "波谱分析"))
        self.name_data_analysis.setText(_translate("data_analysis_module", "数据分析"))

class data_analysis_module(Ui_data_analysis_module):


    def __init__(self, file_modle) -> None:
        self.height_bias = self.height_bias()
        self.horizontal_bias = self.horizontal_bias()
        self.ratio_size =  ratio_size()
        self.app_path = global_value.get_value('app_path').replace('\\','/')
        self.setupUi(file_modle) 

    def height_bias(self) -> float:
        """竖直位置参数修正"""
        bias = 26.5 * ratio_size()
        return bias
    
    def horizontal_bias(self) -> float:
        """水平位置参数修正"""
        bias = 272 * ratio_size()
        return bias


    def module_hide(self):
        """隐藏状态"""
        
        self.Univariate_img.hide()
        self.Univariate_txt.hide()
        self.pushButton_Univariate.hide()
        self.Multivariable_img.hide()
        self.Multivariable_txt.hide()
        self.pushButton_Multivariable.hide()
        self.Spectral_analysis_img.hide()
        self.Spectral_analysis_txt.hide()
        self.pushButton_Spectral_analysis.hide()
        self.line.hide()
        self.line_2.hide()
        self.name_data_analysis.hide()

    def module_show(self):
        """显示状态"""

        self.Univariate_img.show()
        self.Univariate_txt.show()
        self.pushButton_Univariate.show()
        self.Multivariable_img.show()
        self.Multivariable_txt.show()
        self.pushButton_Multivariable.show()
        self.Spectral_analysis_img.show()
        self.Spectral_analysis_txt.show()
        self.pushButton_Spectral_analysis.show()
        self.line.show()
        self.line_2.show()
        self.name_data_analysis.show()
