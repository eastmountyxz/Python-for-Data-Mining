# -*- coding: utf-8 -*-
#载入数据集
from sklearn.datasets import load_iris 
iris = load_iris()
print(iris.data)           #输出数据集
print(iris.target)         #输出真实标签
print(len(iris.target))
print(iris.data.shape)     #150个样本 每个样本4个特征
 
 
#导入决策树DTC包
from sklearn.cluster import KMeans
clf = KMeans(n_clusters=3)
pre = clf.fit_predict(iris.data)      
print(pre)
 
#获取花卉两列数据集
X = iris.data
L1 = [x[0] for x in X]
print(L1)
L2 = [x[1] for x in X]
print(L2)
 
#绘图
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(L1, L2, c=pre, marker='x', s=100) 
plt.title("KMeans")
plt.show()
