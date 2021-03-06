# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 10:55:17 2017
@author: eastmount
"""
 
import pandas as pd
data = pd.read_csv("data.csv",index_col='year') #index_col用作行索引的列名 
#显示前6行数据 
print(data.shape)  
print(data.head(6))
 
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['simHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   #用来正常显示负号
data.plot()
plt.savefig(u'时序图.png', dpi=500)
plt.show()
 
#获取贵阳数据集并绘图
gy = data['Guiyang']
print('输出贵阳数据')
print(gy)
gy.plot()
plt.show()
