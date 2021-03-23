# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:44:19 2016
@author: 杨秀璋
"""
 
#导入数据集iris
from sklearn.datasets import load_iris 
 
#载入数据集
iris = load_iris()
 
print(iris.data)          #输出数据集
print(iris.target)        #输出真实标签
print(len(iris.target))
print(iris.data.shape)    #150个样本 每个样本4个特征
 
 
#导入决策树DTC包
from sklearn.tree import DecisionTreeClassifier
 
#训练
clf = DecisionTreeClassifier()
clf.fit(iris.data, iris.target)
print(clf)
 
#预测
predicted = clf.predict(iris.data)
 
#获取花卉两列数据集
X = iris.data
L1 = [x[0] for x in X]
print(L1)
L2 = [x[1] for x in X]
print(L2)
 
#绘图
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(L1, L2, c=predicted, marker='x')  #cmap=plt.cm.Paired
plt.title("DTC")
plt.show()
