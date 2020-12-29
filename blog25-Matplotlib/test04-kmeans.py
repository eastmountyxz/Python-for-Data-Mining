# -*- coding: utf-8 -*-
#载入数据集
from sklearn.datasets import load_iris 
iris = load_iris()
print(iris.data)            #输出数据集
print(iris.target)          #输出真实标签
print(len(iris.target))
print(iris.data.shape)      #150个样本 每个样本4个特征
 
 
#导入决策树DTC包
from sklearn.cluster import KMeans
clf = KMeans(n_clusters=3)
y_pred = clf.fit_predict(iris.data)      
print(y_pred)
 
#降维绘图
from sklearn.decomposition import PCA
pca = PCA(n_components=2)             #输出两维
newData = pca.fit_transform(iris.data)   #载入N维
print(newData)
x = [n[0] for n in newData]
y = [n[1] for n in newData]
 
x1, y1 = [], []   
x2, y2 = [], [] 
x3, y3 = [], []
    
#分别获取类标为0、1、2的数据 赋值给(x1,y1) (x2,y2) (x3,y3) 
i = 0  
while i < len(newData):  
    if y_pred[i]==0:  
        x1.append(newData[i][0])  
        y1.append(newData[i][1])  
    elif y_pred[i]==1:  
        x2.append(newData[i][0])  
        y2.append(newData[i][1])  
    elif y_pred[i]==2:  
        x3.append(newData[i][0])  
        y3.append(newData[i][1])
    i = i + 1
 
 
import matplotlib.pyplot as plt
 
#三种颜色   
plot1, = plt.plot(x1, y1, 'or', marker="o", markersize=10)    
plot2, = plt.plot(x2, y2, 'og', marker="o", markersize=10)    
plot3, = plt.plot(x3, y3, 'ob', marker="o", markersize=10)
plt.title("K-Means Text Clustering")  #绘制标题
plt.legend((plot1, plot2, plot3), ('A', 'B', 'C'))
 
#plt.scatter(x1, x2, c=clf.labels_,  s=100)
plt.show()
