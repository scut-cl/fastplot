# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\srp\fastplot\project\main_demo\code\ui\file_framework.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from utils.utils import ratio_size
from utils import global_value
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

class Ui_file_module(object):
    """文件模块"""
    
    def __init__(self, file_modle) -> None:
        self.height_bias = self.height_bias()
        self.ratio_size =  ratio_size()
        self.app_path = global_value.get_value('app_path').replace('\\','/')
        self.setupUi(file_modle)     

    def height_bias(self) -> float:
        """竖直位置参数修正"""
        bias = 26.5 * ratio_size()
        return bias

    def setupUi(self, file_modle):
        file_modle.setObjectName("file_modle")
        file_modle.resize(138 * ratio_size(), 51 * ratio_size())
        font = QtGui.QFont()
        font.setFamily("幼圆")
        file_modle.setFont(font)
        file_modle.setStyleSheet("background-color: rgb(171, 171, 171);")
        
        #打开文件
        self.open_file = QtWidgets.QPushButton(file_modle)
        self.open_file.setGeometry(QtCore.QRect(7 * self.ratio_size, 5 * self.ratio_size + self.height_bias, 17 * self.ratio_size, 13 * self.ratio_size))
        self.open_file.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n" +
                                     "border-image: url(" + self.app_path + "/graph/file.png)")
        self.open_file.setText("")
        self.open_file.setObjectName("open_file")
        
        self.open_file_txt = QtWidgets.QLabel(file_modle)
        self.open_file_txt.setGeometry(QtCore.QRect(8 * self.ratio_size, 23 * self.ratio_size + self.height_bias, 17 * self.ratio_size, 12 * self.ratio_size))
        self.open_file_txt.setStyleSheet("background-color: rgb(247, 240, 240);")
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(6 * self.ratio_size)
        self.open_file_txt.setFont(font)
        self.open_file_txt.setObjectName("open_file_txt")
        
        #保存文件
        self.save_file = QtWidgets.QPushButton(file_modle)
        self.save_file.setGeometry(QtCore.QRect(39 * self.ratio_size, 5 * self.ratio_size + self.height_bias, 15 * self.ratio_size, 15 * self.ratio_size))
        self.save_file.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "border-image: url(" + self.app_path + "/graph/save.png)")
        self.save_file.setText("")
        self.save_file.setObjectName("save_file")

        self.save_file_txt = QtWidgets.QLabel(file_modle)
        self.save_file_txt.setGeometry(QtCore.QRect(39 * self.ratio_size, 23 * self.ratio_size + self.height_bias, 15 * self.ratio_size, 12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(6 * self.ratio_size)
        self.save_file_txt.setFont(font)
        self.save_file_txt.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.save_file_txt.setObjectName("save_file_txt")
        
        #新建文件
        self.new_file = QtWidgets.QPushButton(file_modle)
        self.new_file.setGeometry(QtCore.QRect(70 * self.ratio_size, 5 * self.ratio_size + self.height_bias, 15 * self.ratio_size, 15 * self.ratio_size))
        self.new_file.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "border-image: url(" + self.app_path + "/graph/add_file.png)")
        self.new_file.setText("")
        self.new_file.setObjectName("new_file")

        self.new_file_txt = QtWidgets.QLabel(file_modle)
        self.new_file_txt.setGeometry(QtCore.QRect(70 * self.ratio_size, 23 * self.ratio_size + self.height_bias, 15 * self.ratio_size, 12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(6 * self.ratio_size)
        self.new_file_txt.setFont(font)
        self.new_file_txt.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.new_file_txt.setObjectName("new_file_txt")

        #新建表格
        self.new_sheet = QtWidgets.QPushButton(file_modle)
        self.new_sheet.setGeometry(QtCore.QRect(98 * self.ratio_size, 5 * self.ratio_size + self.height_bias, 15 * self.ratio_size, 15 * self.ratio_size))
        self.new_sheet.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "border-image: url(" + self.app_path + "/graph/add_worksheet.png)")
        self.new_sheet.setText("")
        self.new_sheet.setObjectName("new_sheet")

        self.new_sheet_txt = QtWidgets.QLabel(file_modle)
        self.new_sheet_txt.setGeometry(QtCore.QRect(98 * self.ratio_size, 23 * self.ratio_size + self.height_bias, 15 * self.ratio_size, 12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(6 * self.ratio_size)
        self.new_sheet_txt.setFont(font)
        self.new_sheet_txt.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.new_sheet_txt.setObjectName("new_sheet_txt")

        self.new_sheet_txt_2 = QtWidgets.QLabel(file_modle)
        self.new_sheet_txt_2.setGeometry(QtCore.QRect(98 * self.ratio_size, 33 * self.ratio_size + self.height_bias, 15 * self.ratio_size, 12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(6 * self.ratio_size)
        self.new_sheet_txt_2.setFont(font)
        self.new_sheet_txt_2.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.new_sheet_txt_2.setObjectName("new_sheet_txt_2")

        #文件模块名称
        self.name_file = QtWidgets.QLabel(file_modle)
        self.name_file.setGeometry(QtCore.QRect(54 * self.ratio_size, 38 * self.ratio_size + self.height_bias, 17 * self.ratio_size, 12 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(6 * self.ratio_size)
        font.setBold(True)
        font.setWeight(75)
        self.name_file.setFont(font)
        self.name_file.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.name_file.setObjectName("name_file")
        
        #模块分割线
        self.line = QtWidgets.QFrame(file_modle)
        self.line.setGeometry(QtCore.QRect(128 * self.ratio_size, 0 * self.ratio_size + self.height_bias, 5 * self.ratio_size, 48 * self.ratio_size))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setStyleSheet("")
        self.line.setStyleSheet("background-color: rgb(247, 240, 240);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(file_modle)
        QtCore.QMetaObject.connectSlotsByName(file_modle)

    def retranslateUi(self, file_modle):
        _translate = QtCore.QCoreApplication.translate
        file_modle.setWindowTitle(_translate("file_modle", "Form"))
        self.open_file_txt.setText(_translate("file_modle", "打开"))
        self.save_file_txt.setText(_translate("file_modle", "保存"))
        self.new_file_txt.setText(_translate("file_modle", "新建"))
        self.new_sheet_txt.setText(_translate("file_modle", "新建"))
        self.new_sheet_txt_2.setText(_translate("file_modle", "表格"))
        self.name_file.setText(_translate("file_modle", "文件"))

    def module_hide(self):
        """隐藏状态"""

        self.name_file.hide()
        self.open_file.hide()
        self.open_file_txt.hide()
        self.save_file.hide()
        self.save_file_txt.hide()
        self.new_file.hide()
        self.new_file_txt.hide()
        self.new_sheet.hide()
        self.new_sheet_txt.hide()
        self.new_sheet_txt_2.hide()
        self.open_file.hide()
        self.open_file_txt.hide()
        self.line.hide()
    
    def module_show(self):
        """显示状态"""

        self.name_file.show()
        self.open_file.show()
        self.open_file_txt.show()
        self.save_file.show()
        self.save_file_txt.show()
        self.new_file.show()
        self.new_file_txt.show()
        self.new_sheet.show()
        self.new_sheet_txt.show()
        self.new_sheet_txt_2.show()
        self.open_file.show()
        self.open_file_txt.show()
        self.line.show()