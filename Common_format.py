# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\srp\fastplot\project\main_demo\code\ui\Common_format.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from utils.utils import ratio_size
from PyQt5 import QtCore, QtGui, QtWidgets
from utils import global_value


class Ui_common_format_module(object):
    """常用图像格式模块"""

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
        bias = 509 * ratio_size()
        return bias

    def setupUi(self, common_format_module):
        """界面UI"""

        common_format_module.setObjectName("common_format_module")
        common_format_module.resize(339 * self.ratio_size, 49 * self.ratio_size)

        #NMR
        self.pushButton_NMR = QtWidgets.QPushButton(common_format_module)
        self.pushButton_NMR.setGeometry(QtCore.QRect(17 * self.ratio_size + self.horizontal_bias, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_NMR.setStyleSheet("border-image: url(" + self.app_path + "/graph/NMR.png);\n"
                                          "background-color: rgba(255, 255, 255, 0);")
        self.pushButton_NMR.setText("")
        self.pushButton_NMR.setObjectName("pushButton_NMR")

        self.label_NMR = QtWidgets.QLabel(common_format_module)
        self.label_NMR.setGeometry(QtCore.QRect(17 * self.ratio_size + self.horizontal_bias, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_NMR.setFont(font)
        self.label_NMR.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NMR.setObjectName("label_NMR")
        self.label_NMR.setStyleSheet("background-color: rgba(247, 240, 240, 0);")
        
        #IR
        self.label_IR = QtWidgets.QLabel(common_format_module)
        self.label_IR.setGeometry(QtCore.QRect(74 * self.ratio_size + self.horizontal_bias, 30 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 11 * self.ratio_size))
        font = QtGui.QFont()
        font.setPointSize(6 * self.ratio_size)
        self.label_IR.setFont(font)
        self.label_IR.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IR.setObjectName("label_IR")

        self.pushButton_IR = QtWidgets.QPushButton(common_format_module)
        self.pushButton_IR.setGeometry(QtCore.QRect(74 * self.ratio_size + self.horizontal_bias, 3 * self.ratio_size + self.height_bias, 38 * self.ratio_size, 26 * self.ratio_size))
        self.pushButton_IR.setStyleSheet("border-image: url(" + self.app_path + "/graph/IR.png);\n"
                                         "background-color: rgba(255, 255, 255, 0);")
        self.pushButton_IR.setText("")
        self.pushButton_IR.setObjectName("pushButton_IR")
        self.label_IR.setStyleSheet("background-color: rgba(247, 240, 240, 0);")

        #模块名称
        self.name_image_parttern = QtWidgets.QLabel(common_format_module)
        self.name_image_parttern.setGeometry(QtCore.QRect(152 * self.ratio_size + self.horizontal_bias, 38 * self.ratio_size + self.height_bias, 34 * self.ratio_size, 12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(6 * self.ratio_size)
        font.setBold(True)
        font.setWeight(75)
        self.name_image_parttern.setFont(font)
        self.name_image_parttern.setStyleSheet("background-color: rgba(247, 240, 240, 0);")
        self.name_image_parttern.setObjectName("name_image_parttern")
        
        #模块分割线
        self.line = QtWidgets.QFrame(common_format_module)
        self.line.setGeometry(QtCore.QRect(337 * self.ratio_size + self.horizontal_bias, 0 * self.ratio_size + self.height_bias, 5 * self.ratio_size, 48 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(common_format_module)
        QtCore.QMetaObject.connectSlotsByName(common_format_module)

    def retranslateUi(self, common_format_module):
        _translate = QtCore.QCoreApplication.translate
        common_format_module.setWindowTitle(_translate("common_format_module", "Form"))
        self.label_IR.setText(_translate("common_format_module", "IR"))
        self.label_NMR.setText(_translate("common_format_module", "NMR"))
        self.name_image_parttern.setText(_translate("common_format_module", "常用格式"))

    def module_hide(self):
        """隐藏状态"""

        self.pushButton_NMR.hide()
        self.label_NMR.hide()
        self.pushButton_IR.hide()
        self.label_IR.hide()
        self.line.hide()
        self.name_image_parttern.hide() 

    def module_show(self):
        """显示状态"""

        self.pushButton_NMR.show()
        self.label_NMR.show()
        self.pushButton_IR.show()
        self.label_IR.show()
        self.line.show()
        self.name_image_parttern.show() 