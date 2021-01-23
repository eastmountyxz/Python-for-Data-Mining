# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 23:31:16 2017
@author: yxz15
"""
 
# -*- coding: utf-8 -*-
from sklearn.linear_model import LinearRegression
 
#数据集 直径、价格
x = [[5],[6],[7],[8],[10],[11],[13],[14],[16],[18]]
y = [[6],[7.5],[8.6],[9],[12],[13.6],[15.8],[18.5],[19.2],[20]]
print(x)
print(y)
 
clf = LinearRegression()
clf.fit(x,y)
pre = clf.predict([[12]])[0]
print(u'预测直径为12英寸的价格: $%.2f' % pre)
x2 = [[0],[12],[15],[25]]
y2 = clf.predict(x2)
 
import matplotlib.pyplot as plt
import numpy as np
 
plt.figure()
plt.axis([0,25,0,25])
plt.scatter(x,y,marker="s",s=20)
plt.plot(x2,y2,"g-")

#导入多项式回归模型
from sklearn.preprocessing import PolynomialFeatures
xx = np.linspace(0,25,100) #0到25等差数列
quadratic_featurizer = PolynomialFeatures(degree = 4) #实例化一个二次多项式
x_train_quadratic = quadratic_featurizer.fit_transform(x) #用二次多项式多样本x做变换
X_test_quadratic = quadratic_featurizer.transform(x2)
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(x_train_quadratic, y)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))# 把训练好X值的多项式特征实例应用到一系列点上,形成矩阵
 
plt.plot(xx, regressor_quadratic.predict(xx_quadratic),
         label="$y = ax^4 + bx + c$",linewidth=2,color="r")
plt.legend()
plt.show()
