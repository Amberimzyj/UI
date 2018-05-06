# -*- coding: utf-8 -*-
# @Author: Amberimzyj
# @Emial:  amberimzyj@outlook.com
# @Date:   2018-04-29 22:19:10
# @Last Modified by:   Amberimzyj
# @Last Modified time: 2018-05-04 13:58:24
# @License: MIT LICENSE
from matplotlib.backends.backend_qt4agg import FigureCanvas
import matplotlib.pyplot as plt  # 调用绘图库
from matplotlib.figure import Figure
from matplotlib.pyplot import savefig  
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  
import numpy as np


class Matplot(object):
    def __init__(self):
        # 新建一个Figure
        self.figure = Figure()
        # 将Figure转换为Qt4 Widget控件以便插入Qt4界面
        self.canvas = FigureCanvas(self.figure)


    def _change(self, _list1,_list2,_list3):
        # self.figure.clear()
       
        self.x = range(100)
        # y = [100]*100
        # y = [0]*100
        
        self.ax.clear()
        self.ax.plot(self.x,_list1,"y-",linewidth=3,label='Light(lx)')
        self.ax.plot(self.x,_list2,"m-",linewidth=3,label='Tempure(℃)')
        self.ax.plot(self.x,_list3,"c-",linewidth=3,label='Humid(%RH)')
        
        
        #设置图例
        self.ax.legend(loc='upperright')   #   显示图例，loc设置图例位置
        # ax.set_subplots_adjust(bottom = 0.15) 
        

        # self.ax.show()

        # self.figure.suptitle("F3 fata diagram")

        self.canvas.draw()

    def set_diagram(self,n):
        
        
        self.ax = self.figure.add_subplot(111)
        #设置坐标轴范围
        self.ax.set_xlim((0, 110))
        self.ax.set_ylim((0, 150))

        #设置坐标轴刻度
        my_x_ticks = np.arange(0,110, 10)
        my_y_ticks = np.arange(0, 150, 10)

        ymajorLocator   = MultipleLocator(10)
        self.ax.set_xticks(my_x_ticks)
        self.figure.gca().invert_xaxis()
        # self.figure.gca().invert_xticks()
        self.ax.set_yticks(my_y_ticks)
        self.ax.yaxis.set_major_locator(ymajorLocator)
        self.ax.set_xticklabels(('220s','200s','180s','160s','140s','120s','100s','80s','60s','40s','20s'))

        self.figure.subplots_adjust(left=0.05, bottom=0.07, right=0.97, top=0.93,hspace=0.2, wspace=0.2)
        self.ax.set_title('F'+str(n)+'节点数据折线图',fontproperties='SimHei',fontsize=14)
        self.canvas.draw()
  
        
        # self.ax.show()


if __name__ == '__main__':
    test = Matplot()