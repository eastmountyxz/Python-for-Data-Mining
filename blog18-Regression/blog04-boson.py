# -*- coding: utf-8 -*-
from sklearn.datasets import load_boston
import numpy as np
boston = load_boston()
print(boston.data.shape, boston.target.shape)
 
#划分数据集
boston_temp = boston.data[:, np.newaxis, 5]   
x_train = boston_temp[:-100]      #训练样本  
x_test = boston_temp[-100:]       #测试样本 后100行  
y_train = boston.target[:-100]    #训练标记  
y_test = boston.target[-100:]     #预测对比标记
 
#回归分析
from sklearn.linear_model import LinearRegression 
clf = LinearRegression()  
clf.fit(x_train, y_train)  
 
#算法评估
pre = clf.predict(x_test)
print("预测结果", pre)
print("真实结果", y_test)
cost = np.mean(y_test-pre)**2  
print('平方和计算:', cost)
print('系数', clf.coef_)  
print('截距', clf.intercept_)
print('方差', clf.score(x_test, y_test))
 
#绘图分析
import matplotlib.pyplot  as plt
plt.title(u'LinearRegression Boston')     
plt.xlabel(u'x')                   
plt.ylabel(u'price')          
plt.scatter(x_test, y_test, color = 'black')  
plt.plot(x_test, clf.predict(x_test), color='blue', linewidth = 3)
for idx, m in enumerate(x_test):  
    plt.plot([m, m],[y_test[idx],pre[idx]], 'r-')    
plt.show()   
