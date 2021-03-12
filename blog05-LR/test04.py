# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:47:58 2011
@author: Administrator
"""
#第一步 数据集划分
from sklearn import datasets
import numpy as np
 
#获取数据 10*442
d = datasets.load_diabetes()
x = d.data
print('获取x特征')
print(len(x), x.shape)
print(x[:4])
 
#获取一个特征 第3列数据
x_one = x[:,np.newaxis, 2]
print(x_one[:4])
 
#获取的正确结果
y = d.target
print('获取的结果')
print(y[:4])
 
#x特征划分
x_train = x_one[:-42]
x_test = x_one[-42:]
print(len(x_train), len(x_test))
y_train = y[:-42]
y_test = y[-42:]
print(len(y_train), len(y_test))
 
 
#第二步 线性回归实现
from sklearn import linear_model
clf = linear_model.LinearRegression()
print(clf)
clf.fit(x_train, y_train)
pre = clf.predict(x_test)
print('预测结果')
print(pre)
print('真实结果')
print(y_test)
   
   
#第三步 评价结果
cost = np.mean(y_test-pre)**2
print('次方', 2**5)
print('平方和计算:', cost)
print('系数', clf.coef_)
print('截距', clf.intercept_)  
print('方差', clf.score(x_test, y_test))
 
 
#第四步 绘图
import matplotlib.pyplot as plt
plt.title("diabetes")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x_test, y_test, 'k.')
plt.plot(x_test, pre, 'g-')
 
for idx, m in enumerate(x_test):
    plt.plot([m, m],[y_test[idx], 
              pre[idx]], 'r-')
 
plt.savefig('power.png', dpi=300)
 
plt.show()
 
