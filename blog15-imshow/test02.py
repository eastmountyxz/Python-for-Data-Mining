# coding=utf-8
import numpy as np
from pylab import *
from matplotlib import pyplot as plt
 
x = [1, 2, 3, 4]
y = [3, 5, 10, 25]
 
#创建Figure
fig = plt.figure()
 
#创建一个或多个子图(subplot绘图区才能绘图)
ax1 = fig.add_subplot(231)
plt.plot(x, y, marker='D') #绘图及选择子图
plt.sca(ax1)
  
ax2 = fig.add_subplot(232)
plt.scatter(x, y, marker='s', color='r') 
plt.sca(ax2)
plt.grid(True)
 
ax3 = fig.add_subplot(233)
plt.bar(x, y, 0.5, color='c') #柱状图 width=0.5间距
plt.sca(ax3)
 
ax4 = fig.add_subplot(234) 
#高斯分布   
mean = 0  #均值为0   
sigma = 1 #标准差为1 (反应数据集中还是分散的值)  
data = mean+sigma*np.random.randn(10000)
plt.hist(data,40,normed=1,histtype='bar',facecolor='yellowgreen',alpha=0.75)
plt.sca(ax4)
 
m = np.arange(-5.0, 5.0, 0.02)
n = np.sin(m)
ax5 = fig.add_subplot(235)
plt.plot(m, n)
plt.sca(ax5)
 
ax6 = fig.add_subplot(236)
xlim(-2.5, 2.5) #设置x轴范围
ylim(-1, 1)     #设置y轴范围
plt.plot(m, n)
plt.sca(ax6)
plt.grid(True)
 
plt.show()
