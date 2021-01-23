# -*- coding: utf-8 -*-
import numpy as np
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
 
#linspace:开始值、终值和元素个数创建表示等差数列的一维数组
xx, yy = np.meshgrid(np.linspace(0,10,20), np.linspace(0,100,20))
zz = 2.4 * xx + 4.5 * yy + np.random.randint(0,100,(20,20))

#构建成特征、值的形式
X, Z = np.column_stack((xx.flatten(),yy.flatten())), zz.flatten()

#线性回归分析
regr = linear_model.LinearRegression()
regr.fit(X, Z)

#预测的一个特征
x_test = np.array([[15.7, 91.6]])
print(regr.predict(x_test))

#画图可视化分析
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(xx, yy, zz) #真实点

#拟合的平面
ax.plot_wireframe(xx, yy, regr.predict(X).reshape(20,20))
ax.plot_surface(xx, yy, regr.predict(X).reshape(20,20), alpha=0.3)
plt.show()
