# -*- coding: utf-8 -*-
#第一部分 载入数据集
import pandas as pd
X = pd.read_csv("seed_x.csv")
Y = pd.read_csv("seed_y.csv")
print(X)
print(Y)
 
#第二部分 导入模型
from sklearn.naive_bayes import GaussianNB  
clf = GaussianNB()
clf.fit(X, Y)      
pre = clf.predict(X)
print("数据集预测结果:", pre)
 
#第三部分 降维处理
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
newData = pca.fit_transform(X)
print(newData[:4])
 
#第四部分 绘制图形
import matplotlib.pyplot as plt
L1 = [n[0] for n in newData]
L2 = [n[1] for n in newData]
plt.scatter(L1,L2,c=pre,s=200)
plt.show()
