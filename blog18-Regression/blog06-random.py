# -*- coding: utf-8 -*-
import numpy as np
import math
 
#随机数生成
X =  np.arange(0,50,0.2) 
print(X)
xArr = []
yArr = []
for n in X:
    xArr.append(n)
    y = 0.7*n + np.random.uniform(0,1)*math.sin(n)*2 - 3
    yArr.append(y)
 
#线性回归分析
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
print(clf)
X =  np.array(X).reshape((len(X),1))     #list转化为数组
yArr = np.array(yArr).reshape((len(X),1))
clf.fit(X,yArr)
pre = clf.predict(X)
 
import matplotlib.pyplot as plt
plt.plot(X, yArr, 'go')
plt.plot(X, pre, 'r', linewidth=3)
plt.show()
