# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris = load_iris()
clf = KMeans()
clf.fit(iris.data, iris.target)
print(clf)
predicted = clf.predict(iris.data)

#获取花卉两列数据集  
X = iris.data
L1 = [x[0] for x in X]
print(L1)
L2 = [x[1] for x in X]  
print(L2)

import numpy as np
import matplotlib.pyplot as plt
plt.scatter(L1, L2, c=predicted, marker='s',s=200,cmap=plt.cm.Paired)
plt.title("Iris")
plt.show()
