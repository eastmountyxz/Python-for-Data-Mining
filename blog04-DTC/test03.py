# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:44:19 2016
@author: 杨秀璋
"""
 
#导入数据集iris
from sklearn.datasets import load_iris
import numpy as np
 
#载入数据集
iris = load_iris()
 
'''
print iris.data          #输出数据集
print iris.target        #输出真实标签
print len(iris.target)
print iris.data.shape    #150个样本 每个样本4个特征
'''
 
'''
重点：分割数据集 构造训练集/测试集，120/30
     70%训练  0-40  50-90  100-140
     30%预测  40-50 90-100 140-150
'''
#训练集
train_data = np.concatenate((iris.data[0:40, :], iris.data[50:90, :], iris.data[100:140, :]), axis = 0)
#训练集样本类别
train_target = np.concatenate((iris.target[0:40], iris.target[50:90], iris.target[100:140]), axis = 0)
#测试集
test_data = np.concatenate((iris.data[40:50, :], iris.data[90:100, :], iris.data[140:150, :]), axis = 0)
#测试集样本类别
test_target = np.concatenate((iris.target[40:50], iris.target[90:100], iris.target[140:150]), axis = 0)
 
 
#导入决策树DTC包
from sklearn.tree import DecisionTreeClassifier
 
#训练
clf = DecisionTreeClassifier()
#注意均使用训练数据集和样本类标
clf.fit(train_data, train_target)
print(clf)
 
#预测结果
predict_target = clf.predict(test_data)
print(predict_target)
 
#预测结果与真实结果比对
print(sum(predict_target == test_target))
 
#输出准确率 召回率 F值
from sklearn import metrics
print(metrics.classification_report(test_target, predict_target))
print(metrics.confusion_matrix(test_target, predict_target))
 
 
#获取花卉测试数据集两列数据集
X = test_data
L1 = [n[0] for n in X]
print(L1)
L2 = [n[1] for n in X]
print(L2)
 
#绘图
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(L1, L2, c=predict_target, marker='x')  #cmap=plt.cm.Paired
plt.title("DecisionTreeClassifier")
plt.show()
