# -*- coding: utf-8 -*-
from sklearn.linear_model import LinearRegression
 
#数据集 直径、价格
x = [[5],[6],[7],[8],[10],[11],[13],[14],[16],[18]]
y = [[6],[7.5],[8.6],[9],[12],[13.6],[15.8],[18.5],[19.2],[20]]
print(x)
print(y)

clf = LinearRegression()
clf.fit(x,y)
pre = clf.predict([[12]])[0]
print(u'预测直径为12英寸的价格: $%.2f' % pre)
