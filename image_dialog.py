# -*- coding: utf-8 -*-

# 2022/3/21 apply_params函数返回属性值既麻烦也无必要

from typing import Tuple
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QColorDialog
from utils import global_value
from utils.utils import data_obtain

class Ui_Dialog(object):
    """绘图参数对话框UI"""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(417, 452)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(3, -1, 411, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.apply_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.apply_Button.setObjectName("apply_Button")
        self.gridLayout.addWidget(self.apply_Button, 1, 1, 1, 1)
        self.dialog_tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.dialog_tabWidget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.dialog_tabWidget.setObjectName("dialog_tabWidget")
        self.fig_tab = QtWidgets.QWidget()
        self.fig_tab.setObjectName("fig_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.fig_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 402, 388))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.x_min_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.x_min_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_min_edit.setObjectName("x_min_edit")
        self.gridLayout_2.addWidget(self.x_min_edit, 1, 7, 1, 1)
        self.x_max_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.x_max_title.setAlignment(QtCore.Qt.AlignCenter)
        self.x_max_title.setObjectName("x_max_title")
        self.gridLayout_2.addWidget(self.x_max_title, 2, 3, 1, 1)
        self.fontComboBox = QtWidgets.QFontComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_2.addWidget(self.fontComboBox, 16, 7, 1, 1)
        self.z_tick_direction_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.z_tick_direction_title.setAlignment(QtCore.Qt.AlignCenter)
        self.z_tick_direction_title.setObjectName("z_tick_direction_title")
        self.gridLayout_2.addWidget(self.z_tick_direction_title, 14, 3, 1, 1)
        self.x_tick_direction_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.x_tick_direction_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_tick_direction_comboBox.setObjectName("x_tick_direction_comboBox")
        self.gridLayout_2.addWidget(self.x_tick_direction_comboBox, 4, 7, 1, 1)
        self.x_tick_direction_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.x_tick_direction_title.setObjectName("x_tick_direction_title")
        self.gridLayout_2.addWidget(self.x_tick_direction_title, 4, 3, 1, 1)
        self.x_tick_value_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.x_tick_value_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_tick_value_edit.setObjectName("x_tick_value_edit")
        self.gridLayout_2.addWidget(self.x_tick_value_edit, 3, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 8, 1, 1)
        self.z_max_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.z_max_title.setAlignment(QtCore.Qt.AlignCenter)
        self.z_max_title.setObjectName("z_max_title")
        self.gridLayout_2.addWidget(self.z_max_title, 12, 3, 1, 1)
        self.z_max_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.z_max_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.z_max_edit.setObjectName("z_max_edit")
        self.gridLayout_2.addWidget(self.z_max_edit, 12, 7, 1, 1)
        self.z_tick_value_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.z_tick_value_title.setAlignment(QtCore.Qt.AlignCenter)
        self.z_tick_value_title.setObjectName("z_tick_value_title")
        self.gridLayout_2.addWidget(self.z_tick_value_title, 13, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.y_min_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.y_min_title.setAlignment(QtCore.Qt.AlignCenter)
        self.y_min_title.setObjectName("y_min_title")
        self.gridLayout_2.addWidget(self.y_min_title, 6, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 0, 1, 9)
        self.x_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.x_title.setFont(font)
        self.x_title.setObjectName("x_title")
        self.gridLayout_2.addWidget(self.x_title, 1, 1, 4, 1)
        self.y_tick_direction_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.y_tick_direction_title.setObjectName("y_tick_direction_title")
        self.gridLayout_2.addWidget(self.y_tick_direction_title, 9, 3, 1, 1)
        self.fig_color_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.fig_color_Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fig_color_Button.setText("")
        self.fig_color_Button.setObjectName("fig_color_Button")
        self.gridLayout_2.addWidget(self.fig_color_Button, 17, 4, 1, 1)
        self.x_tick_value_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.x_tick_value_title.setAlignment(QtCore.Qt.AlignCenter)
        self.x_tick_value_title.setObjectName("x_tick_value_title")
        self.gridLayout_2.addWidget(self.x_tick_value_title, 3, 3, 1, 1)
        self.y_max_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.y_max_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_max_edit.setObjectName("y_max_edit")
        self.gridLayout_2.addWidget(self.y_max_edit, 7, 7, 1, 1)
        self.z_tick_direction_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.z_tick_direction_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.z_tick_direction_comboBox.setObjectName("z_tick_direction_comboBox")
        self.gridLayout_2.addWidget(self.z_tick_direction_comboBox, 14, 7, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 15, 1, 1, 8)
        self.y_tick_value_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.y_tick_value_title.setAlignment(QtCore.Qt.AlignCenter)
        self.y_tick_value_title.setObjectName("y_tick_value_title")
        self.gridLayout_2.addWidget(self.y_tick_value_title, 8, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 5, 1, 1, 8)
        self.z_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.z_title.setFont(font)
        self.z_title.setObjectName("z_title")
        self.gridLayout_2.addWidget(self.z_title, 11, 1, 4, 1)
        self.fig_color_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.fig_color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_color_label.setObjectName("fig_color_label")
        self.gridLayout_2.addWidget(self.fig_color_label, 17, 3, 1, 1)
        self.z_min_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.z_min_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.z_min_edit.setObjectName("z_min_edit")
        self.gridLayout_2.addWidget(self.z_min_edit, 11, 7, 1, 1)
        self.fig_title_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.fig_title_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fig_title_edit.setObjectName("fig_title_edit")
        self.gridLayout_2.addWidget(self.fig_title_edit, 16, 3, 1, 2)
        self.y_tick_value_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.y_tick_value_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_tick_value_edit.setObjectName("y_tick_value_edit")
        self.gridLayout_2.addWidget(self.y_tick_value_edit, 8, 7, 1, 1)
        self.x_min_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.x_min_title.setFont(font)
        self.x_min_title.setAlignment(QtCore.Qt.AlignCenter)
        self.x_min_title.setObjectName("x_min_title")
        self.gridLayout_2.addWidget(self.x_min_title, 1, 3, 1, 1)
        self.z_min_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.z_min_title.setAlignment(QtCore.Qt.AlignCenter)
        self.z_min_title.setObjectName("z_min_title")
        self.gridLayout_2.addWidget(self.z_min_title, 11, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 10, 1, 1, 8)
        spacerItem4 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        self.y_max_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.y_max_title.setAlignment(QtCore.Qt.AlignCenter)
        self.y_max_title.setObjectName("y_max_title")
        self.gridLayout_2.addWidget(self.y_max_title, 7, 3, 1, 1)
        self.fig_title_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fig_title_label.setFont(font)
        self.fig_title_label.setObjectName("fig_title_label")
        self.gridLayout_2.addWidget(self.fig_title_label, 16, 1, 1, 1)
        self.y_tick_direction_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.y_tick_direction_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_tick_direction_comboBox.setObjectName("y_tick_direction_comboBox")
        self.gridLayout_2.addWidget(self.y_tick_direction_comboBox, 9, 7, 1, 1)
        self.x_max_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.x_max_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_max_edit.setObjectName("x_max_edit")
        self.gridLayout_2.addWidget(self.x_max_edit, 2, 7, 1, 1)
        self.y_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.y_title.setFont(font)
        self.y_title.setObjectName("y_title")
        self.gridLayout_2.addWidget(self.y_title, 6, 1, 4, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 17, 1, 1, 1)
        self.z_tick_value_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.z_tick_value_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.z_tick_value_edit.setObjectName("z_tick_value_edit")
        self.gridLayout_2.addWidget(self.z_tick_value_edit, 13, 7, 1, 1)
        self.y_min_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.y_min_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_min_edit.setObjectName("y_min_edit")
        self.gridLayout_2.addWidget(self.y_min_edit, 6, 7, 1, 1)
        self.legend_edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.legend_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.legend_edit.setObjectName("legend_edit")
        self.gridLayout_2.addWidget(self.legend_edit, 17, 7, 1, 1)
        self.legend_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.legend_checkbox.setObjectName("legend_checkbox")
        self.gridLayout_2.addWidget(self.legend_checkbox, 17, 6, 1, 1)
        self.font_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.font_title.setFont(font)
        self.font_title.setObjectName("font_title")
        self.gridLayout_2.addWidget(self.font_title, 16, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 14, 5, 1, 1)
        self.dialog_tabWidget.addTab(self.fig_tab, "")
        self.line_scatter_tab = QtWidgets.QWidget()
        self.line_scatter_tab.setObjectName("line_scatter_tab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.line_scatter_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 401, 211))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scatter_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.scatter_label.setFont(font)
        self.scatter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scatter_label.setObjectName("scatter_label")
        self.gridLayout_3.addWidget(self.scatter_label, 0, 0, 3, 1)
        self.line_color_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.line_color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.line_color_label.setObjectName("line_color_label")
        self.gridLayout_3.addWidget(self.line_color_label, 7, 1, 1, 1)
        self.line_style_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.line_style_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_style_comboBox.setObjectName("line_style_comboBox")
        self.gridLayout_3.addWidget(self.line_style_comboBox, 4, 2, 1, 1)
        self.connect_style_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.connect_style_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.connect_style_comboBox.setObjectName("connect_style_comboBox")
        self.gridLayout_3.addWidget(self.connect_style_comboBox, 5, 2, 1, 1)
        self.scatter_style_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.scatter_style_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scatter_style_label.setObjectName("scatter_style_label")
        self.gridLayout_3.addWidget(self.scatter_style_label, 0, 1, 1, 1)
        self.line_width_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.line_width_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_width_comboBox.setObjectName("line_width_comboBox")
        self.gridLayout_3.addWidget(self.line_width_comboBox, 6, 2, 1, 1)
        self.scatter_style_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.scatter_style_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scatter_style_comboBox.setObjectName("scatter_style_comboBox")
        self.gridLayout_3.addWidget(self.scatter_style_comboBox, 0, 2, 1, 1)
        self.scatter_color_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.scatter_color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scatter_color_label.setObjectName("scatter_color_label")
        self.gridLayout_3.addWidget(self.scatter_color_label, 2, 1, 1, 1)
        self.scatter_size_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.scatter_size_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scatter_size_comboBox.setObjectName("scatter_size_comboBox")
        self.gridLayout_3.addWidget(self.scatter_size_comboBox, 1, 2, 1, 1)
        self.line_tilte = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_tilte.setFont(font)
        self.line_tilte.setAlignment(QtCore.Qt.AlignCenter)
        self.line_tilte.setObjectName("line_tilte")
        self.gridLayout_3.addWidget(self.line_tilte, 4, 0, 4, 1)
        self.line_width_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.line_width_label.setAlignment(QtCore.Qt.AlignCenter)
        self.line_width_label.setObjectName("line_width_label")
        self.gridLayout_3.addWidget(self.line_width_label, 6, 1, 1, 1)
        self.connect_style_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.connect_style_label.setAlignment(QtCore.Qt.AlignCenter)
        self.connect_style_label.setObjectName("connect_style_label")
        self.gridLayout_3.addWidget(self.connect_style_label, 5, 1, 1, 1)
        self.scatter_size_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.scatter_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scatter_size_label.setObjectName("scatter_size_label")
        self.gridLayout_3.addWidget(self.scatter_size_label, 1, 1, 1, 1)
        self.line_style_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.line_style_label.setAlignment(QtCore.Qt.AlignCenter)
        self.line_style_label.setObjectName("line_style_label")
        self.gridLayout_3.addWidget(self.line_style_label, 4, 1, 1, 1)
        self.scatter_style_replay = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.scatter_style_replay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scatter_style_replay.setText("")
        self.scatter_style_replay.setObjectName("scatter_style_replay")
        self.gridLayout_3.addWidget(self.scatter_style_replay, 0, 3, 3, 1)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 3, 0, 1, 3)
        self.scatter_color_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.scatter_color_Button.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.scatter_color_Button.setText("")
        self.scatter_color_Button.setObjectName("scatter_color_Button")
        self.gridLayout_3.addWidget(self.scatter_color_Button, 2, 2, 1, 1)
        self.line_color_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.line_color_Button.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_color_Button.setText("")
        self.line_color_Button.setObjectName("line_color_Button")
        self.gridLayout_3.addWidget(self.line_color_Button, 7, 2, 1, 1)
        self.dialog_tabWidget.addTab(self.line_scatter_tab, "")
        self.gridLayout.addWidget(self.dialog_tabWidget, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.dialog_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.apply_Button.setText(_translate("Dialog", "应用"))
        self.x_max_title.setText(_translate("Dialog", "右值"))
        self.z_tick_direction_title.setText(_translate("Dialog", "刻度线方向"))
        self.x_tick_direction_title.setText(_translate("Dialog", "刻度线方向"))
        self.z_max_title.setText(_translate("Dialog", "右值"))
        self.z_tick_value_title.setText(_translate("Dialog", "分度值"))
        self.y_min_title.setText(_translate("Dialog", "左值"))
        self.x_title.setText(_translate("Dialog", "x轴"))
        self.y_tick_direction_title.setText(_translate("Dialog", "刻度线方向"))
        self.x_tick_value_title.setText(_translate("Dialog", "分度值"))
        self.y_tick_value_title.setText(_translate("Dialog", "分度值"))
        self.z_title.setText(_translate("Dialog", "z轴"))
        self.fig_color_label.setText(_translate("Dialog", "画布颜色"))
        self.x_min_title.setText(_translate("Dialog", "左值"))
        self.z_min_title.setText(_translate("Dialog", "左值"))
        self.y_max_title.setText(_translate("Dialog", "右值"))
        self.fig_title_label.setText(_translate("Dialog", "标题"))
        self.y_title.setText(_translate("Dialog", "y轴"))
        self.legend_checkbox.setText(_translate("Dialog", "图例"))
        self.font_title.setText(_translate("Dialog", "字体"))
        self.dialog_tabWidget.setTabText(self.dialog_tabWidget.indexOf(self.fig_tab), _translate("Dialog", "画布与坐标轴"))
        self.scatter_label.setText(_translate("Dialog", "数据点"))
        self.line_color_label.setText(_translate("Dialog", "颜色"))
        self.scatter_style_label.setText(_translate("Dialog", "样式"))
        self.scatter_color_label.setText(_translate("Dialog", "颜色"))
        self.line_tilte.setText(_translate("Dialog", "连接线"))
        self.line_width_label.setText(_translate("Dialog", "线宽"))
        self.connect_style_label.setText(_translate("Dialog", "连接样式"))
        self.scatter_size_label.setText(_translate("Dialog", "大小"))
        self.line_style_label.setText(_translate("Dialog", "线形"))
        self.dialog_tabWidget.setTabText(self.dialog_tabWidget.indexOf(self.line_scatter_tab), _translate("Dialog", "点型与线型"))


class image_dialog(QDialog, Ui_Dialog):
    """绘图参数对话框"""

    def __init__(self,parent=None) -> Tuple:

        super(image_dialog, self).__init__(parent)
       
        self.setupUi(self)

        self.combox_additem()
        self._init_params()
        
        self.widget_action()
        #print('ready')
        self.exec_()    
        
    
    def _init_params(self):
        """初始化参数"""

        # x轴参数
        data_array = data_obtain()
        self.x_min = float(min(data_array[:, 0]))
        self.x_max = float(max(data_array[:, 0]))
        self.x_tick_value = (float(max(data_array[:, 0])) - float(min(data_array[:, 0])))/5
        self.x_tick_direction = 'in'
        
        # y轴参数
        self.y_min = float(min(data_array[:, 1]))
        self.y_max = float(max(data_array[:, 1]))
        self.y_tick_value = (float(max(data_array[:, 1])) - float(min(data_array[:, 1])))/5
        self.y_tick_direction = 'in'
        
        # z轴参数
        try:
            self.z_min = float(min(data_array[:, 2]))
            self.z_max = float(max(data_array[:, 2]))
            self.z_tick_value = (float(max(data_array[:, 2])) - float(min(data_array[:, 2])))/5
        except:
            self.z_min = float(0)
            self.z_max = float(10)            
            self.z_tick_value = float(2)
        self.z_tick_direction = 'in'
        #标题参数
        self.fig_title = ' '  
        self.fig_font = 6
        
        #图例布尔值
        self.legend_bool = False
        self.legend_txt = 'plot figure'
        self.fig_color = '#ffffff'
        
        #数据点参数
        self.scatter_style = 'square marker'
        self.scatter_size= '5'
        self.scatter_color = '#000000'

        #连接线参数
        self.line_style = '———————'
        self.connect_style = 1
        self.line_width = 0.2
        self.line_color = '#000000'


    def apply_params(self):
        """获取绘图参数 
        (x_min:float, x_max:float, x_tick_value:float, x_tick_direction:str, 
         y_min:float, y_max:float, y_tick_value:float, y_tick_direction:str,
         z_min:float, z_max:float, z_tick_value:float, z_tick_direction:str, 
         fig_title, fig_font:float, legend_bool:bool, fig_color:str,
         scatter_style:str, scatter_size:float, scatter_color:str, 
         line_style:str, connect_style:str, line_width:float, line_color:str,self.legend_txt:str)"""
        
        # x轴参数
        try:
            self.x_min = float(self.x_min_edit.text())
            self.x_max = float(self.x_max_edit.text())
            self.x_tick_value = float(self.x_tick_value_edit.text())
        except:
            pass
        self.x_tick_direction = self.x_tick_direction_comboBox.currentText()
        
        # y轴参数
        try:
            self.y_min = float(self.y_min_edit.text())
            self.y_max = float(self.y_max_edit.text())
            self.y_tick_value = float(self.y_tick_value_edit.text())
        except:
            pass        
        self.y_tick_direction = self.y_tick_direction_comboBox.currentText()
        
        # z轴参数
        try:
            self.z_min = float(self.z_min_edit.text())
            self.z_max = float(self.z_max_edit.text())
            self.z_tick_value = float(self.z_tick_value_edit.text())
        except:
            pass
        self.z_tick_direction = self.z_tick_direction_comboBox.currentText()
        
        #标题参数
        self.fig_title = self.fig_title_edit.text()        
        self.fig_font = self.fontComboBox.currentText()
        
        #图例布尔值
        self.legend_bool = self.legend_checkbox.isChecked()
        self.legend_txt = self.legend_edit.text()    

        #数据点参数
        self.scatter_style = self.maker_dict[self.scatter_style_comboBox.currentText()]
        self.scatter_size= float(self.scatter_size_comboBox.currentText())
        
        #连接线参数
        self.line_style = self.line_dict[self.line_style_comboBox.currentText()]
        self.connect_style = self.connect_style_dict[self.connect_style_comboBox.currentText()]
        self.line_width = float(self.line_width_comboBox.currentText())
        
        self.close()       


    def widget_action(self):
        '''控件事件'''

        self.fig_color_Button.clicked.connect(self.fig_color_select)
        self.scatter_color_Button.clicked.connect(self.scatter_color_select)
        self.line_color_Button.clicked.connect(self.line_color_select)
        self.apply_Button.clicked.connect(self.apply_params)
        self.scatter_style_comboBox.activated[str].connect(self.maker_change)
    

    def fig_color_select(self):
        """画布颜色"""
        color = QColorDialog.getColor()
        self.fig_color = color.name()
        #print(type(self.fig_color))
        self.fig_color_Button.setStyleSheet("background-color: {};".format(self.fig_color))


    def scatter_color_select(self):
        """数据点颜色"""
        color = QColorDialog.getColor()
        self.scatter_color = color.name()
        self.scatter_color_Button.setStyleSheet("background-color: {};".format(self.scatter_color))
 
    def line_color_select(self):
        """线条颜色"""
        color = QColorDialog.getColor()
        self.line_color = color.name()
        self.line_color_Button.setStyleSheet("background-color: {};".format(self.line_color))

    def combox_additem(self):
        """添加下拉内容"""

        self.x_tick_direction_comboBox.addItems(['in', 'out', 'inout'])
        self.y_tick_direction_comboBox.addItems(['in', 'out', 'inout'])
        self.z_tick_direction_comboBox.addItems(['in', 'out', 'inout'])
        marker_list = ['hline marker', 'vline marker', 'thin diamond marker', 'diamond marker', 'x marker',
                       'plus marker', 'hexagon2 marker', 'hexagon1 marker', 'star marker', 'pentagon marker',
                       'square marker', 'tri right marker', 'tri left marker', 'tri up marker', 'tri down marker', 'triangle right marker',
                       'triangle left marker', 'triangle_up marker', 'triangle down marker', 'circle marker', 'pixel marker', 'point marker']
        markerstyleList = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+','x', 'D', 'd', '|', '_']
        self.maker_dict = {}
        for i in range(22):
            self.maker_dict[marker_list[i]] = markerstyleList[21 - i]
        print(self.maker_dict['square marker'])

        maker_szie = ['0', '1', '3', '5', '8', '12', '15', '18', '24', '30']
        self.scatter_style_comboBox.addItems(marker_list)
        self.scatter_size_comboBox.addItems(maker_szie)

        line_list = ['·······', '-·-·-·-·-', '- - - - - - -', '———————']
        self.line_dict = {'·······':":", '-·-·-·-·-':"-.", '- - - - - - -':"--", '———————':"-"}

        line_width = ['0.2', '0.5', '1', '1.5', '2', '3', '4', '5']
        self.line_style_comboBox.addItems(line_list)
        self.line_width_comboBox.addItems(line_width)

        connect_style = ['直线', 'B样条曲线']
        self.connect_style_dict = {'直线': 0, 'B样条曲线':1}
        self.connect_style_comboBox.addItems(connect_style)


    def maker_change(self):
        """改变数据点图片"""

        name = self.scatter_style_comboBox.currentText()

        app_path = global_value.get_value('app_path').replace('\\','/') + '/graph/maker/' + name + '.png'

        jpg = QtGui.QPixmap(app_path)
        self.scatter_style_replay.setPixmap(jpg)


