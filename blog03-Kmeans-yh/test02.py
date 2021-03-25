# -*- coding: utf-8 -*-
 
"""
By: Eastmount CSDN 2016-10-12
该部分讲数据集读取，然后赋值给X变量
读取文件data.txt 保存结果为X
"""
 
import os
 
data = []
for line in open("data.txt", "r").readlines():
    line = line.rstrip()    #删除换行
    #删除多余空格，保存一个空格连接
    result = ' '.join(line.split())
    #获取每行五个值 '0 0.0888 201 36.02 28 0.5885' 注意：字符串转换为浮点型数
    s = [float(x) for x in result.strip().split(' ')]
    #输出结果：['0', '0.0888', '201', '36.02', '28', '0.5885']
    print(s)
    #数据存储至data
    data.append(s)
 
#输出完整数据集
print('完整数据集')
print(data)
print(type(data))
 
'''
现在输出数据集：
['0 0.0888 201 36.02 28 0.5885', 
 '1 0.1399 198 39.32 30 0.8291', 
 '2 0.0747 198 38.80 26 0.4974', 
 '3 0.0983 191 40.71 30 0.5772', 
 '4 0.1276 196 38.40 28 0.5703'
]
'''
 
print('第一列 第五列数据')
L2 = [n[0] for n in data]
print(L2)
L5 = [n[4] for n in data]
print(L5)
 
'''
X表示二维矩阵数据，篮球运动员比赛数据
总共96行，每行获取两列数据
第一列表示球员每分钟助攻数：assists_per_minute
第五列表示球员每分钟得分数：points_per_minute
'''
 
#两列数据生成二维数据
print('两列数据合并成二维矩阵')
T = dict(zip(L2,L5))
type(T)
 
#dict类型转换为list
print('List')
X = list(map(lambda x,y: (x,y), T.keys(),T.values()))
print(X)
print(type(X))
 
 
"""
KMeans聚类
clf = KMeans(n_clusters=3) 表示类簇数为3，聚成3类数据，clf即赋值为KMeans
y_pred = clf.fit_predict(X) 载入数据集X，并且将聚类的结果赋值给y_pred
"""
 
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
 
clf = KMeans(n_clusters=3)
y_pred = clf.fit_predict(X)
print(clf)
#输出聚类预测结果，96行数据，每个y_pred对应X一行或一个球员，聚成3类，类标为0、1、2
print(y_pred)
 
 
"""
可视化绘图
Python导入Matplotlib包，专门用于绘图
import matplotlib.pyplot as plt 此处as相当于重命名，plt用于显示图像
"""
 
import numpy as np
import matplotlib.pyplot as plt
 
 
#获取第一列和第二列数据 使用for循环获取 n[0]表示X第一列
x = [n[0] for n in X]
print(x)
y = [n[1] for n in X]
print(y) 
 
#绘制散点图 参数：x横轴 y纵轴 c=y_pred聚类预测结果 marker类型 o表示圆点 *表示星型 x表示点
#plt.scatter(x, y, c=y_pred, marker='x')
 
 
#坐标
x1 = []
y1 = []
 
x2 = []
y2 = []
 
x3 = []
y3 = []
 
#分布获取类标为0、1、2的数据 赋值给(x1,y1) (x2,y2) (x3,y3)
i = 0
while i < len(X):
    if y_pred[i]==0:
        x1.append(X[i][0])
        y1.append(X[i][1])
    elif y_pred[i]==1:
        x2.append(X[i][0])
        y2.append(X[i][1])
    elif y_pred[i]==2:
        x3.append(X[i][0])
        y3.append(X[i][1])
    
    i = i + 1
 
 
#四种颜色 红 绿 蓝 黑  
plot1, = plt.plot(x1, y1, 'or', marker="x")  
plot2, = plt.plot(x2, y2, 'og', marker="o")  
plot3, = plt.plot(x3, y3, 'ob', marker="*")  
 
#绘制标题
plt.title("Kmeans-Basketball Data")
 
#绘制x轴和y轴坐标
plt.xlabel("assists_per_minute")
plt.ylabel("points_per_minute")
 
#设置右上角图例
plt.legend((plot1, plot2, plot3), ('A', 'B', 'C'), fontsize=10)
 
plt.show()  
