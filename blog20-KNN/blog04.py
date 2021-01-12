# -*- coding: utf-8 -*-
import os 
import numpy as np
 
#第一步 导入数据集
data = np.loadtxt("wine.txt",dtype=str,delimiter=",")
print(data)
print(type(data))
yy, x = np.split(data, (1,), axis=1)
print(yy.shape, x.shape)
#从字符型转换为Int整型
X = x.astype(int)
#获取x两列数据,方便绘图 对应x、y轴
X = X[:, 1:3]  
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
 
#第二步 KNN分析
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
print(knn)
knn.fit(X,y)
pre = knn.predict(X)
print(pre)
 
#第三步 数据评估  
from sklearn import metrics  
print(sum(pre == y))   #预测结果与真实结果比对
print(metrics.classification_report(y,pre))   #输出准确率 召回率 F值  
print(metrics.confusion_matrix(y,pre)) 
 
#第四步 创建网格 
x1_min, x1_max = X[:,0].min()-0.1, X[:,0].max()+0.1  #第一列
x2_min, x2_max = X[:,1].min()-0.1, X[:,1].max()+0.1  #第二列
xx, yy = np.meshgrid(np.arange(x1_min, x1_max, 0.1),  
                     np.arange(x2_min, x2_max, 0.1))  #生成网格型数据
print(xx.shape, yy.shape) #(42L, 42L) (42L, 42L)
print(xx.ravel().shape, yy.ravel().shape)  #(1764L,) (1764L,)
print(np.c_[xx.ravel(), yy.ravel()].shape) #合并 (1764L, 2L)
#ravel()拉直函数
z = knn.predict(np.c_[xx.ravel(), yy.ravel()])    
print(z)
 
#第五步 绘图可视化
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])   #颜色Map
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
plt.figure()
z = z.reshape(xx.shape)                
plt.pcolormesh(xx, yy, z, cmap=cmap_light)
plt.scatter(X[:,0], X[:,1], c=y, cmap=cmap_bold, s=50)
plt.show()
