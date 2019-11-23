# -*- coding: utf-8 -*-  
import os
import csv
import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn import neighbors

#-----------------------------------------第一步 加载数据集-----------------------------------------
fr= open("kddcup.data_10_percent_corrected-result-minmax.csv")
lines = fr.readlines()
line_nums = len(lines)
print(line_nums)

#创建line_nums行 para_num列的矩阵
x_mat = np.zeros((line_nums, 41))
y_label = []

#划分数据集
for i in range(line_nums):
    line = lines[i].strip()
    item_mat = line.split(',')
    x_mat[i, :] = item_mat[0:41]    #前41个特征
    y_label.append(item_mat[-1])  #类标
fr.close()
print x_mat.shape
print len(y_label)


#-----------------------------------------第二步 划分数据集-----------------------------------------
y = []
for n in y_label: 
    y.append(int(float(n)))
y =  np.array(y, dtype = int) #list转换数组

#划分数据集 测试集40%
train_data, test_data, train_target, test_target = train_test_split(x_mat, y, test_size=0.4, random_state=42)
print train_data.shape, train_target.shape
print test_data.shape, test_target.shape


#-----------------------------------------第三步 KNN训练-----------------------------------------
clf = neighbors.KNeighborsClassifier()
clf.fit(train_data, train_target)
print clf
result = clf.predict(test_data)
print result
print test_target


#-----------------------------------------第四步 评价算法-----------------------------------------
print sum(result==test_target) #预测结果与真实结果比对
print(metrics.classification_report(test_target, result))  #准确率 召回率 F值


#----------------------------------------第五步 降维可视化---------------------------------------
pca = PCA(n_components=2)      
newData = pca.fit_transform(test_data)
plt.figure()
plt.scatter(newData[:,0], newData[:,1], c=test_target, s=50)
plt.show()
