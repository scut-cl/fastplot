import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MatplotlibWidget(FigureCanvas):
    """matpotlib控件, 需要定义 plot_dunction (绘图函数)"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['font.family'] = ['sans-serif']
        plt.rcParams['font.size'] = 15
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        self.plot_function()
        
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)        
    
    def plot_function(self):
        """定义绘图函数"""
        raise NotImplementedError()

