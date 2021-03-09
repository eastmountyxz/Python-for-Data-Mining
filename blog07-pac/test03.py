# -*- coding: utf-8 -*-
 
#糖尿病数据集
from sklearn.datasets import load_diabetes
data = load_diabetes()
x = data.data
print(x[:4])
y = data.target
print(y[:4])
 
#KMeans聚类算法
from sklearn.cluster import KMeans
#训练
clf = KMeans(n_clusters=2)
print(clf)
clf.fit(x)
#预测
pre = clf.predict(x)
print(pre[:10])
 
#使用PCA降维操作
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
newData = pca.fit_transform(x)
print(newData[:4])
 
L1 = [n[0] for n in newData]
L2 = [n[1] for n in newData]
 
#绘图
import numpy as np
import matplotlib.pyplot as plt
 
#用来正常显示中文标签
plt.rc('font', family='SimHei', size=8)
#plt.rcParams['font.sans-serif']=['SimHei'] 
 
#用来正常显示负号
plt.rcParams['axes.unicode_minus']=False 
 
p1 = plt.subplot(221)
plt.title(u"Kmeans聚类 n=2")
plt.scatter(L1,L2,c=pre,marker="s")
plt.sca(p1)
 
 
###################################
# 聚类 类蔟数=3
 
clf = KMeans(n_clusters=3)
clf.fit(x)
pre = clf.predict(x)
 
p2 = plt.subplot(222)
plt.title("Kmeans n=3")
plt.scatter(L1,L2,c=pre,marker="s")
plt.sca(p2)
 
 
###################################
# 聚类 类蔟数=4
 
clf = KMeans(n_clusters=4)
clf.fit(x)
pre = clf.predict(x)
 
p3 = plt.subplot(223)
plt.title("Kmeans n=4")
plt.scatter(L1,L2,c=pre,marker="+")
plt.sca(p3)
 
 
###################################
# 聚类 类蔟数=5
 
clf = KMeans(n_clusters=5)
clf.fit(x)
pre = clf.predict(x)
 
p4 = plt.subplot(224)
plt.title("Kmeans n=5")
plt.scatter(L1,L2,c=pre,marker="+")
plt.sca(p4)
 
#保存图片本地
plt.savefig('power.png', dpi=300)  
plt.show()
 
