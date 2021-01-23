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
print('预测直径为12英寸的价格: $%.2f' % pre)
x2 = [[0],[12],[15],[25]]
y2 = clf.predict(x2)
 
import matplotlib.pyplot as plt
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.title(u"线性回归预测Pizza直径和价格")
plt.xlabel(u"x")
plt.ylabel(u"price")
plt.axis([0,25,0,25])
plt.scatter(x,y,marker="s",s=20)
plt.plot(x2,y2,"g-")
plt.show()
