# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 04:06:01 2016
@author: yxz15
"""
 
#导入数据集
import pandas as pd
data = pd.read_excel("data.xls", header=None) 
mm = data.sum()
print('计算用电量总数:')
print(mm)
 
#绘制图形
import numpy as np
import matplotlib.pyplot as plt
#中文字体显示
plt.rc('font', family='SimHei', size=13)
N = 3
#3个用户 0 1 2
ind = np.arange(N)  # the x locations for the groups 
print(ind)
#设置宽度
width = 0.35        
x = [u'用户A', u'用户B', u'用户C']
#绘图
plt.bar(ind, mm, width, color='r', label='sum num')
plt.xlabel(u"用户名")
plt.ylabel(u"总耗电量")
plt.title(u'电力窃漏电用户自动识别--总耗电量')
plt.legend()
#设置底部名称
plt.xticks(ind+width/2, x, rotation=40) #旋转40度
plt.show()
 
