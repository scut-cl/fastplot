
from sqlite3 import DataError
from typing import List, Tuple
import matplotlib
from matplotlib.ticker import MultipleLocator

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from utils.utils import ratio_size,data_obtain, data_normalize
from scipy.interpolate import make_interp_spline, interp1d
import numpy as np

class MatplotlibWidget(FigureCanvas):
    """matpotlib控件, 需要定义 plot_dunction (绘图函数)"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        

        
        plt.rcParams['font.family'] = ['sans-serif']
        plt.rcParams['font.size'] = 7 * ratio_size()
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


        self.fig = Figure(figsize=(width, height), dpi=dpi)# 新建一个figure
          
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(111)# 建立一个子图，如果要建立复合图，可以在这里修改

        self.setParent(parent)        

    
    def plot_function(self):
        """定义绘图函数"""
        raise NotImplementedError()

class Scatter_graph(MatplotlibWidget):
    """散点图"""
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       

        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params

    def plot_function(self):   

        data_array = data_obtain()
        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)#fontstyle = paint_params[13]
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色
        self.axes.scatter(data_array[:, 0], #x轴数据
                          data_array[:, 1], #y轴数据
                          marker=self.paint_params.scatter_style, #点格式
                          s=self.paint_params.scatter_size, #点大小
                          c=self.paint_params.scatter_color,#点颜色
                          label = self.paint_params.legend_txt) 
        #print('paint_params[23]', paint_params[23])

        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        self.axes.set_ylim(self.paint_params.y_min, self.paint_params.y_max)
        self.axes.set_xlim(self.paint_params.x_min, self.paint_params.x_max)

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 


        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  
         
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False) 

class Solidline_graph(MatplotlibWidget):
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       

        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params

    def plot_function(self):
        
        data_array = data_obtain()

        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        x = data_array[:, 0]
        y = data_array[:, 1]


        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色

        if self.paint_params.connect_style == 0: #折线
            self.axes.plot(x,
                           y,
                           marker=self.paint_params.scatter_style, #点格式
                           ms=self.paint_params.scatter_size, #点大小
                           mfc=self.paint_params.scatter_color,#点颜色
                           ls = self.paint_params.line_style, #线格式
                           lw = self.paint_params.line_width,  #线宽
                           c = self.paint_params.line_color,   #线颜色
                           label = self.paint_params.legend_txt) 

        elif self.paint_params.connect_style == 1: #B样条
            x_smooth = np.linspace(min(x), max(x), len(x) * 10)
            #print(x)
            #y_smooth = make_interp_spline(x, y)(x_smooth)       
            func = interp1d(x, y, kind='cubic')
            # 利用xnew和func函数生成ynew，xnew的数量等于ynew数量
            y_smooth = func(x_smooth)

            self.axes.scatter(data_array[:, 0], #x轴数据
                              data_array[:, 1], #y轴数据
                              marker=self.paint_params.scatter_style, #点格式
                              s=self.paint_params.scatter_size, #点大小
                              c=self.paint_params.scatter_color) #点颜色   

            self.axes.plot(x_smooth,
                           y_smooth,
                           ls = self.paint_params.line_style, #线格式
                           lw = self.paint_params.line_width,  #线宽
                           c = self.paint_params.line_color,   #线颜色
                           label = self.paint_params.legend_txt) 
        
        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 

        self.axes.set_ylim(self.paint_params.y_min, self.paint_params.y_max)
        self.axes.set_xlim(self.paint_params.x_min, self.paint_params.x_max)

        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  

        #self.axes.set_ylim(0, 1)
        #self.axes.set_xlim(210, 360)
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)         


class fitting_graph(MatplotlibWidget):

    """拟合曲线绘图, 传入: 绘图参数, 拟合数据"""
    
    def __init__(self, paint_params, fit_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       

        super().__init__(parent, width, height, dpi)
        
        self.paint_params = paint_params
        self.fit_params = fit_params

    def plot_function(self):
    
        data_array = data_obtain()
        #x = data_array[:, 0]
        #y = data_array[:, 1]

        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)
            
        self.axes.scatter(data_array[:, 0], #x轴数据
                          data_array[:, 1], #y轴数据
                          marker=self.paint_params.scatter_style, #点格式
                          s=self.paint_params.scatter_size, #点大小
                          c=self.paint_params.scatter_color) #点颜色   

        self.axes.plot(self.fit_params.x_fitting,
                       self.fit_params.y_fitting,
                       ls = self.paint_params.line_style, #线格式
                       lw = self.paint_params.line_width,  #线宽
                       c = self.paint_params.line_color,   #线颜色
                       label = self.paint_params.legend_txt) 
        
        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例
        #设置主刻度标签的位置

        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 

        self.axes.set_ylim(self.paint_params.y_min, self.paint_params.y_max)
        self.axes.set_xlim(self.paint_params.x_min, self.paint_params.x_max)
        

        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  

        #self.axes.set_ylim(0, 1)
        #self.axes.set_xlim(210, 360)
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)                 


class Bar_graph(MatplotlibWidget):
    """柱状图"""
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       

        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params

    def plot_function(self):   

        data_array = data_obtain()
        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)#fontstyle = paint_params[13]
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色
        self.axes.bar(data_array[:, 0], #x轴数据
                      data_array[:, 1], #y轴数据
                      align = 'center', #对齐方式
                      color=self.paint_params.line_color,#点颜色
                      label = self.paint_params.legend_txt) 
        #print('paint_params[23]', paint_params[23])

        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        self.axes.set_ylim(self.paint_params.y_min, self.paint_params.y_max)
        self.axes.set_xlim(self.paint_params.x_min, self.paint_params.x_max)

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 


        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  
         
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)         

class Step_graph(MatplotlibWidget):
    """阶梯图"""
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       

        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params

    def plot_function(self):   

        data_array = data_obtain()
        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)#fontstyle = paint_params[13]
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色
        self.axes.step(data_array[:, 0], #x轴数据
                      data_array[:, 1], #y轴数据
                      where = 'pre', #对齐方式
                      color=self.paint_params.line_color,#点颜色
                      lw = self.paint_params.line_width,  #线宽
                      label = self.paint_params.legend_txt) 
        #print('paint_params[23]', paint_params[23])

        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        self.axes.set_ylim(self.paint_params.y_min, self.paint_params.y_max)
        self.axes.set_xlim(self.paint_params.x_min, self.paint_params.x_max)

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 


        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  
         
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)         

class Stem_graph(MatplotlibWidget):
    """垂线图"""
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       


        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params

    def plot_function(self):   

        data_array = data_obtain()

        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)#fontstyle = paint_params[13]
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色

        self.axes.scatter(data_array[:, 0], #x轴数据
                          data_array[:, 1], #y轴数据
                          marker=self.paint_params.scatter_style, #点格式
                          s=self.paint_params.scatter_size, #点大小
                          c=self.paint_params.scatter_color) #点颜色   
        
        for i, x in enumerate(data_array[:, 0]):
            x_stem = [x, x]
            y_stem = [data_array[:, 1][i], 0]
            
            self.axes.plot(x_stem,
                           y_stem,
                           ls = self.paint_params.line_style, #线格式
                           lw = self.paint_params.line_width,  #线宽
                           c = self.paint_params.line_color,   #线颜色
                           label = self.paint_params.legend_txt) 


        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        self.axes.set_ylim(self.paint_params.y_min, self.paint_params.y_max)
        self.axes.set_xlim(self.paint_params.x_min, self.paint_params.x_max)

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 


        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  
         
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)         
        
class Threedimension_graph(MatplotlibWidget):
    """三维图"""
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       
        
        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params
        self.axes = self.fig.add_subplot(111, projection='3d') 

    def plot_function(self):
        
        data_array = data_obtain()

        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        x = data_array[:, 0]
        y = data_array[:, 1]
        z = data_array[:, 2]

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色

        if self.paint_params.connect_style == 0: #折线

            self.axes.scatter3D(x, #x轴数据
                                y, #y轴数据
                                z,  #z轴数据
                                marker=self.paint_params.scatter_style, #点格式
                                s=self.paint_params.scatter_size, #点大小
                                c=self.paint_params.scatter_color) #点颜色   

            self.axes.plot3D(x,
                             y,
                             z,
                             ls = self.paint_params.line_style, #线格式
                             lw = self.paint_params.line_width,  #线宽
                             c = self.paint_params.line_color,   #线颜色
                             label = self.paint_params.legend_txt) 

        elif self.paint_params.connect_style == 1: #B样条
 
            
            x_smooth, y_smooth, z_smooth = self.smooth_data(x, y, z) 


            self.axes.scatter3D(x, #x轴数据
                                y, #y轴数据
                                z, #z轴数据
                                marker=self.paint_params.scatter_style, #点格式
                                s=self.paint_params.scatter_size, #点大小
                                c=self.paint_params.scatter_color) #点颜色   

            self.axes.plot3D(x_smooth,
                             y_smooth,
                             z_smooth,
                             ls = self.paint_params.line_style, #线格式
                             lw = self.paint_params.line_width,  #线宽
                             c = self.paint_params.line_color,   #线颜色
                             label = self.paint_params.legend_txt) 
        
        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 


        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  

        #self.axes.set_ylim(0, 1)
        #self.axes.set_xlim(210, 360)
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)     
    
    def smooth_data(self, x, y, z) -> Tuple:
        
        
        x_expend = np.linspace(min(x), max(x), len(x) * 10)

        y_smooth = make_interp_spline(x, y)(x_expend) 
        z_smooth = make_interp_spline(x, z)(x_expend) 
        

        return (x_expend, y_smooth, z_smooth)


class Error_graph(MatplotlibWidget):
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       

        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params

    def plot_function(self):
        
        data_array = data_obtain()

        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        x = data_array[:, 0]
        y = data_array[:, 1]
        
        #print('y.size ', y.size)
        n = y.size

        y_std = np.std(y)
        y_se = y_std / np.sqrt(n)

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色

        if self.paint_params.connect_style == 0: #折线
            self.axes.errorbar(x,
                               y,
                               yerr = y_se,
                               marker=self.paint_params.scatter_style, #点格式
                               ms=self.paint_params.scatter_size, #点大小
                               mfc=self.paint_params.scatter_color,#点颜色
                               ls = self.paint_params.line_style, #线格式
                               lw = self.paint_params.line_width,  #线宽
                               c = self.paint_params.line_color,   #线颜色
                               label = self.paint_params.legend_txt) 

        elif self.paint_params.connect_style == 1: #B样条
            x_smooth = np.linspace(min(x), max(x), len(x) * 10)
            #print(x)
            #y_smooth = make_interp_spline(x, y)(x_smooth)       
            func = interp1d(x, y, kind='cubic')
            # 利用xnew和func函数生成ynew，xnew的数量等于ynew数量
            y_smooth = func(x_smooth)

            self.axes.scatter(data_array[:, 0], #x轴数据
                              data_array[:, 1], #y轴数据
                              marker=self.paint_params.scatter_style, #点格式
                              s=self.paint_params.scatter_size, #点大小
                              c=self.paint_params.scatter_color) #点颜色   
            
            self.axes.errorbar(x,
                               y,
                               yerr = y_se,
                               ls = self.paint_params.line_style, #线格式
                               lw = 0,  #线宽
                               c = self.paint_params.line_color,   #线颜色
                               ecolor = self.paint_params.line_color, #误差棒颜色
                               elinewidth = self.paint_params.line_width, #误差棒宽
                               label = self.paint_params.legend_txt) 
            
            self.axes.plot(x_smooth,
                           y_smooth,
                           ls = self.paint_params.line_style, #线格式
                           lw = self.paint_params.line_width,  #线宽
                           c = self.paint_params.line_color,   #线颜色
                           label = self.paint_params.legend_txt) 

        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 


        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  

        #self.axes.set_ylim(0, 1)
        #self.axes.set_xlim(210, 360)
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)         


class Histogram3D_graph(MatplotlibWidget):
    """三维柱状"""
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = paint_params.x_tick_direction #x轴刻度线方向
        plt.rcParams['ytick.direction'] = paint_params.y_tick_direction #y轴刻度线方向       
        
        super().__init__(parent, width, height, dpi)
        self.paint_params = paint_params
        self.axes = self.fig.add_subplot(111, projection='3d') 

    def plot_function(self):   

        data_array = data_obtain()

        xmajorLocator  = MultipleLocator(self.paint_params.x_tick_value) #x主刻度标签设置
        xminorLocator  = MultipleLocator(self.paint_params.x_tick_value/5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(self.paint_params.y_tick_value) #x主刻度标签设置
        yminorLocator  = MultipleLocator(self.paint_params.y_tick_value/5) #x轴次刻度标签设置        

        self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)#fontstyle = paint_params[13]
        self.fig.set_facecolor(self.paint_params.fig_color) #画布颜色
        
        xpos, ypos, zpos, dx, dy, dz = self.get_data(data_array)

        self.axes.bar3d(xpos, ypos, zpos, dx, dy, dz, color=self.paint_params.line_color, zsort='average')

        if self.paint_params.legend_bool:
            self.axes.legend()  #添加图例

        #self.axes.set_ylim(self.paint_params.y_min, self.paint_params.y_max)
        #self.axes.set_xlim(self.paint_params.x_min, self.paint_params.x_max)

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 


        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  
         
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(False)    
    
    def get_data(self, data):

        xedges, yedges = np.array([i + 1 for i in range(data.shape[0] + 1)]), np.array([i + 1 for i in range(data.shape[1] + 1)])
        
        
        xpos, ypos = np.meshgrid(xedges[:-1] , yedges[:-1] )
        xpos = xpos.flatten('F')
        ypos = ypos.flatten('F')
        zpos = np.zeros_like(xpos)
        #print(xpos, ypos)
        #设置柱形图大小
        dx =self.paint_params.line_width * np.ones_like(zpos)
        dy = dx.copy()
        dz = data.flatten() 
        #print(xpos.shape, ypos.shape, zpos.shape, dx.shape, dy.shape, dz.shape)

        return xpos, ypos, zpos, dx, dy, dz


import ternary

class Ternary_graph(FigureCanvas):
    """三角图"""
    
    def __init__(self, paint_params, parent=None, width=5, height=4, dpi=100):#
        

        
        plt.rcParams['font.family'] = ['sans-serif']
        plt.rcParams['font.size'] = 7 * ratio_size()
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        self.paint_params = paint_params

        self.fig, self.tax = ternary.figure(scale=self.paint_params.x_max)# 新建一个figure
          
        FigureCanvas.__init__(self, self.fig)
        #self.axes = self.fig.add_subplot(111)# 建立一个子图，如果要建立复合图，可以在这里修改

        self.setParent(parent)        

    def plot_function(self):   

        data = data_normalize(data_obtain(), self.paint_params.x_max)

        #pos_data = self.get_data(data)
        

        self.tax.boundary(linewidth = 1 * ratio_size())        #图框宽度
        self.tax.gridlines(color = 'black',     #网格线颜色
                           multiple = self.paint_params.x_tick_value, #网格线分度值
                           linewidth = 0.5 * ratio_size(),    #网格线宽
                           alpha = 0.7 * ratio_size())        #透明度

        self.tax.gridlines(color = 'b',     #网格线颜色
                           multiple = self.paint_params.x_tick_value/5, #网格线分度值
                           linewidth = 0.2,    #网格线宽
                           alpha = 0.4)        #透明度        


        fontsize = 7 * ratio_size()
        self.tax.set_title("Simplex Boundary and Gridlines", fontsize=fontsize)
        self.tax.left_axis_label("Left label $\\alpha^2$", fontsize=fontsize)
        self.tax.right_axis_label("Right label $\\beta^2$", fontsize=fontsize)
        self.tax.bottom_axis_label("Bottom label $\\Gamma - \\Omega$", fontsize=fontsize)

        self.tax.scatter(data, 
                         marker=self.paint_params.scatter_style, 
                         s=self.paint_params.scatter_size,
                         color=self.paint_params.scatter_color, 
                         label=self.paint_params.legend_txt)

        if self.paint_params.connect_style == 0: #折线

            for seq in range(len(data) - 1):

                self.tax.line(data[seq], 
                              data[seq + 1], 
                              linewidth=self.paint_params.line_width, 
                              color=self.paint_params.scatter_color, 
                              linestyle=self.paint_params.line_style,)

        elif self.paint_params.connect_style == 1: #B样条

            self.tax.plot(data, 
                           ls = self.paint_params.line_style, #线格式
                           lw = self.paint_params.line_width,  #线宽
                           c = self.paint_params.line_color,   #线颜色
                           label = self.paint_params.legend_txt) 


        # Set ticks
        self.tax.ticks(axis='lbr', 
                       linewidth=1 * ratio_size(), 
                       multiple = self.paint_params.x_tick_value, #刻度分度值
                       fontsize = 3 * ratio_size(), 
                       offset = 0.01 * ratio_size(),
                       tick_formats="%.1f")

        self.tax.clear_matplotlib_ticks()
    
    def get_data(self, data) -> List[Tuple]:
        """转换数据类型"""

        try:
            data_list = []
            for col in range(len(data.shape[0])):
                data_list.append((data[col, 0], data[col, 1], data[col, 2]))
            
            return data_list
        
        except:
            raise DataError

class IR_graph(MatplotlibWidget):

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = 'out' #x轴刻度线方向
        plt.rcParams['ytick.direction'] = 'out' #y轴刻度线方向       

        super().__init__(parent, width, height, dpi)

    def plot_function(self):
        
        data_array = data_obtain()

        xmajorLocator  = MultipleLocator(1000) #x主刻度标签设置
        xminorLocator  = MultipleLocator(200) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(50) #x主刻度标签设置
        yminorLocator  = MultipleLocator(10) #x轴次刻度标签设置        

        x = data_array[:, 0]
        y = data_array[:, 1]


        #self.fig.suptitle(self.paint_params.fig_title, font = self.paint_params.fig_font)
        self.fig.set_facecolor('white') #画布颜色

        x_smooth = np.linspace(min(x), max(x), len(x) * 10)
 
        func = interp1d(x, y, kind='cubic')
        # 利用xnew和func函数生成ynew，xnew的数量等于ynew数量
        y_smooth = func(x_smooth)

        self.axes.plot(x_smooth,
                       y_smooth,
                       ls = "-", #线格式
                       lw = 1 * ratio_size(),  #线宽
                       c = 'black',   #线颜色
                       ) 
        

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 

        self.axes.set_ylim(0, 100)
        self.axes.set_xlim(4000, 400)
        

        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  

        self.axes.set_ylabel("%Transmittance")
        self.axes.set_xlabel("Wavenumbers($cm^-$$^1$)")
        self.axes.grid(False)         

class NMR_graph(MatplotlibWidget):
    """NMR图"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['xtick.direction'] = 'out' #x轴刻度线方向
        plt.rcParams['ytick.direction'] = 'out' #y轴刻度线方向     
          

        super().__init__(parent, width, height, dpi)

    def plot_function(self):
        
        data_array = data_obtain()
        
        x = data_array[:, 0]
        y = data_array[:, 1]

        xmajorLocator  = MultipleLocator(1) #x主刻度标签设置
        xminorLocator  = MultipleLocator(0.5) #x轴次刻度标签设置
        ymajorLocator  = MultipleLocator(max(y)/5) #y主刻度标签设置
        yminorLocator  = MultipleLocator(max(y)/10) #y轴次刻度标签设置        

        self.fig.set_facecolor('white') #画布颜色

        x_smooth = np.linspace(min(x), max(x), len(x) * 10)
 
        func = interp1d(x, y, kind='cubic')
        # 利用xnew和func函数生成ynew，xnew的数量等于ynew数量
        y_smooth = func(x_smooth)

        self.axes.plot(x_smooth,
                       y_smooth,
                       ls = "-", #线格式
                       lw = 1 * ratio_size(),  #线宽
                       c = 'black',   #线颜色
                       ) 
        

        #设置主刻度标签的位置
        self.axes.xaxis.set_major_locator(xmajorLocator) 
        self.axes.yaxis.set_major_locator(ymajorLocator) 
        self.axes.yaxis.tick_right()

        self.axes.set_ylim(-max(y) * 1/5, max(y) * 6/5)
        self.axes.set_xlim(max(x), min(x))
        # 隐藏左侧和顶端的坐标轴
        self.axes.spines['left'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        #self.axes.tick_params(top=False,labeltop=False,labelright = True, labelleft = False)
        #self.axes.tick_params(which = 'minor', top=False,labeltop=False,labelright = True, labelleft = False)
        #显示次刻度标签的位置
        self.axes.xaxis.set_minor_locator(xminorLocator) 
        self.axes.yaxis.set_minor_locator(yminorLocator)  

        #self.axes.set_ylabel("%Transmittance")
        self.axes.set_xlabel("$\\delta(ppm)$")
        self.axes.grid(color = 'gray', linewidth = 0.5, alpha = 0.5)         
