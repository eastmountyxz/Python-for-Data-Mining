# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 10:55:17 2017
@author: yxz15
"""
 
import pandas as pd
data = pd.read_csv("data.csv",index_col='year')
#显示前6行数据  
print(data.shape)  
print(data.head(6))
 
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['simHei']
plt.rcParams['axes.unicode_minus'] = False
data.plot()
plt.savefig(u'时序图.png', dpi=500)
plt.show()
 
from statsmodels.graphics.tsaplots import plot_acf
gy = data['Guiyang']
print(gy)
plot_acf(gy).show()
plt.savefig(u'贵阳自相关图',dpi=300)
 
from statsmodels.tsa.stattools import adfuller as ADF
print('ADF:',ADF(gy))
