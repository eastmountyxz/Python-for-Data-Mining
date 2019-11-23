# -*- coding: utf-8 -*-  
import os
import csv
import numpy as np
from sklearn.svm import SVC  
from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn import neighbors

#-----------------------------------------第一步 加载数据集-----------------------------------------
fr= open("kddcup.data_10_yxz-result-minmax.csv")
lines = fr.readlines()
line_nums = len(lines)
print(line_nums)

#创建line_nums行 para_num列的矩阵
x_mat = np.zeros((line_nums, 31))
y_label = []

#划分数据集
for i in range(line_nums):
    line = lines[i].strip()
    item_mat = line.split(',')
    x_mat[i, :] = item_mat[0:31]    #前41个特征
    y_label.append(item_mat[-1])  #类标
fr.close()
print(x_mat.shape)
print(len(y_label))

#-----------------------------------------第二步 划分数据集-----------------------------------------
y = []
for n in y_label: 
    y.append(int(float(n)))
y =  np.array(y, dtype = int) #list转换数组

#划分数据集 测试集40%
train_data, test_data, train_target, test_target = train_test_split(x_mat, y, test_size=0.4, random_state=42)
print(train_data.shape, train_target.shape)
print(test_data.shape, test_target.shape)


#-----------------------------------------第三步 KNN训练-----------------------------------------
def classify(input_vct, data_set):
    data_set_size = data_set.shape[0]
    #扩充input_vct到与data_set同型并相减
    diff_mat = np.tile(input_vct, (data_set_size, 1)) - data_set  
    sq_diff_mat = diff_mat**2                          #矩阵中每个元素都平方
    distance = sq_diff_mat.sum(axis=1)**0.5  #每行相加求和并开平方根
    return distance.min(axis=0)                         #返回最小距离

test_size = len(test_target)
result = np.zeros((test_size, 3))
for i in range(test_size):
    #序号 最小欧氏距离 测试集数据类别
    result[i] = i + 1, classify(test_data[i], train_data), test_target[i]
#矩阵转置
result = np.transpose(result)  
    
#-----------------------------------------第四步 评价及可视化-----------------------------------------
def roc(data_set):
    normal = 0
    data_set_size = data_set.shape[1]
    roc_rate = np.zeros((2, data_set_size)) #输出ROC曲线 二维矩阵
    #计算正常请求数量
    for i in range(data_set_size):
        if data_set[2][i] == 1:
            normal += 1
    abnormal = data_set_size - normal
    max_dis = data_set[1].max()               #欧式距离最大值
    for j in range(1000):
        threshold = max_dis / 1000 * j
        normal1 = 0
        abnormal1 = 0
        for k in range(data_set_size):
            if data_set[1][k] > threshold and data_set[2][k] == 1:
                normal1 += 1
            if data_set[1][k] > threshold and data_set[2][k] != 1:
                abnormal1 += 1
        roc_rate[0][j] = normal1 / normal           # 阈值以上正常点/全体正常的点
        roc_rate[1][j] = abnormal1 / abnormal   # 阈值以上异常点/全体异常点
    return roc_rate

#图1 散点图
#横轴为序号 纵轴为最小欧氏距离
#点中心颜色根据测试集数据类别而定 点外围无颜色 点大小为最小1 灰度为最大1
plt.figure(1)
plt.scatter(result[0], result[1], c=result[2], edgecolors='None', s=2, alpha=1)

#图2 ROC曲线
#横轴误报率：即阈值以上正常点/全体正常的点
#纵轴检测率：即阈值以上异常点/全体异常点
roc_rate = roc(result)
plt.figure(2)
plt.scatter(roc_rate[0], roc_rate[1], edgecolors='None', s=1, alpha=1)    
plt.show()



