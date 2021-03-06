# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 10:19:15 2017
@author: yxz15
"""
 
#第一部分：导入数据集
import pandas as pd
Coke1 =pd.read_csv("data2.csv")
print(Coke1 [:4])
 
#第二部分：聚类
from sklearn.cluster import KMeans
clf=KMeans(n_clusters=3)
pre=clf.fit_predict(Coke1)
print(pre[:4])
 
#第三部分：降维
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
newData=pca.fit_transform(Coke1)
print(newData[:4])
x1=[n[0] for n in newData]
x2=[n[1] for n in newData]
 
#第四部分：用matplotlib包画图
import matplotlib.pyplot as plt
plt.title
plt.xlabel("x feature")
plt.ylabel("y feature")
plt.scatter(x1,x2,c=pre, marker='x')
plt.savefig("bankloan.png",dpi=400)
plt.show()
