# -*- coding: utf-8 -*-
import os 
import numpy as np
data = np.loadtxt("wine.txt",dtype=str,delimiter=",")
print(data)
print(type(data))
 
yy, x = np.split(data, (1,), axis=1)
print(yy.shape, x.shape)
print(x)
print(yy[:5])
 
#从字符型转换为Int整型
X = x.astype(int)
print(X)
#字母转换为数字
y = []
i = 0
print(len(yy))
while i<len(yy):
    if yy[i]=="L":
        y.append(0)
    elif yy[i]=="B":
        y.append(1)
    elif yy[i]=="R":
        y.append(2)
    i = i + 1
print(y[:5])
 
#KNN分析
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
print(knn)
knn.fit(X,y)
pre = knn.predict(X)
print(pre)
 
#可视化分析
import matplotlib.pyplot as plt
L1 = [x[0] for x in X]
L2 = [x[2] for x in X]
plt.scatter(L1, L2, c=pre, marker='s', s=200)
plt.show()
