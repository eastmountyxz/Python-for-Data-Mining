# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 18:10:07 2017
@author: eastmount & zj
"""
 
#导入玻璃识别数据集
import pandas as pd
glass=pd.read_csv("glass.csv")
#显示前6行数据
print(glass.shape)
print(glass.head(6))
 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(font_scale=1.5)
sns.lmplot(x='al', y='ri', data=glass, ci=None)
#利用Pandas画散点图
glass.plot(kind='scatter', x='al', y='ri')
plt.show()
 
#利用matplotlib做等效的散点图
plt.scatter(glass.al, glass.ri)
plt.xlabel('al')
plt.ylabel('ri')
 
#拟合线性回归模型
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
feature_cols = ['al']
X = glass[feature_cols]
y = glass.ri
linreg.fit(X, y)
plt.show()
 
#对于所有的x值做出预测       
glass['ri_pred'] = linreg.predict(X)
print("预测的前六行:")
print(glass.head(6))
 
#用直线表示预测结果
plt.plot(glass.al, glass.ri_pred, color='red')
plt.xlabel('al')
plt.ylabel('Predicted ri')
plt.show()
 
#将直线结果和散点图同时显示出来
plt.scatter(glass.al, glass.ri)
plt.plot(glass.al, glass.ri_pred, color='red')
plt.xlabel('al')
plt.ylabel('ri')
plt.show()
 
#利用相关方法线性预测
linreg.intercept_ + linreg.coef_ * 2
#使用预测方法计算Al = 2的预测
linreg.predict(2)
 
#铝检验系数
ai=zip(feature_cols, linreg.coef_)
print(ai)
 
#使用预测方法计算Al = 3的预测
pre=linreg.predict(3)
print(pre)
 
#检查glass_type
sort=glass.glass_type.value_counts().sort_index()
print(sort)
 
#类型1、2、3的窗户玻璃
#类型5，6，7是家用玻璃
glass['household'] = glass.glass_type.map({1:0, 2:0, 3:0, 5:1, 6:1, 7:1})
print(glass.head())
 
plt.scatter(glass.al, glass.household)
plt.xlabel('al')
plt.ylabel('household')
plt.show()
 
#拟合线性回归模型并存储预测
feature_cols = ['al']
X = glass[feature_cols]
y = glass.household
linreg.fit(X, y)
glass['household_pred'] = linreg.predict(X)
plt.show()
 
#包括回归线的散点图
plt.scatter(glass.al, glass.household)
plt.plot(glass.al, glass.household_pred, color='red')
plt.xlabel('al')
plt.ylabel('household')
plt.show()
 
