# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 00:44:55 2016
@author: yxz15
"""
 
from sklearn import linear_model       #导入线性模型
import matplotlib.pyplot as plt        #绘图
import numpy as np
 
#X表示匹萨尺寸 Y表示匹萨价格
X = [[6], [8], [10], [14], [18]]
Y = [[7], [9], [13], [17.5], [18]]
 
print('数据集X: ', X)
print('数据集Y: ', Y)
 
#回归训练
clf = linear_model.LinearRegression() #使用线性回归
clf.fit(X, Y)                         #导入数据集
res = clf.predict(np.array([12]).reshape(-1, 1))[0] #预测结果
print('预测一张12英寸匹萨价格：$%.2f' % res)
 
#预测结果
X2 = [[0], [10], [14], [25]]
Y2 = clf.predict(X2)
 
#绘制线性回归图形
plt.figure()
plt.title(u'diameter-cost curver')   #标题
plt.xlabel(u'diameter')              #x轴坐标
plt.ylabel(u'cost')                  #y轴坐标
plt.axis([0, 25, 0, 25])             #区间
plt.grid(True)                       #显示网格
plt.plot(X, Y, 'k.')                 #绘制训练数据集散点图
plt.plot(X2, Y2, 'g-')               #绘制预测数据集直线
plt.show()
 
