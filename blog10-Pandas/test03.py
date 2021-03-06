# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 10:55:17 2017
@author: eastmount
"""
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("data.csv",index_col='year') #index_col用作行索引的列名 
#显示前6行数据 
print(data.shape)  
print(data.head(6))
#获取贵阳数据集并绘图
gy = data['Guiyang']
print('输出贵阳数据')
print(gy)
 
import numpy as np
x = ['2002','2003','2004','2005','2006','2007','2008',
     '2009','2010','2011','2012','2013','2014']
N = 13
ind = np.arange(N)  #赋值0-13
width=0.35
plt.bar(ind, gy, width, color='r', label='sum num') 
#设置底部名称  
plt.xticks(ind+width/2, x, rotation=40) #旋转40度  
plt.title('The price of Guiyang')  
plt.xlabel('year')  
plt.ylabel('price')  
plt.savefig('guiyang.png',dpi=400)  
plt.show()
