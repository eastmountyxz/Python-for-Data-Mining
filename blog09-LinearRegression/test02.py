# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 18:28:56 2017
@author: eastmount & zj
"""
#导入玻璃识别数据集
import pandas as pd
glass=pd.read_csv("glass.csv")
print(glass.shape)
print(glass.head(6))
 
#拟合Logistic回归模型 存储类预测
import numpy as np
nums = np.array([5, 15, 8])
np.where(nums > 10, 'big', 'small')  
#将household_pred转换为 1或0   
glass['household_pred_class'] = np.where(glass.household_pred >= 0.5, 1, 0)
print(glass.head(6))

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
feature_cols = ['al']
X = glass[feature_cols]
y = glass.household
logreg.fit(X, y)
glass['household_pred_class'] = logreg.predict(X)
 
 
#绘图-显示预测结果
plt.scatter(glass.al, glass.household)
plt.plot(glass.al, glass.household_pred_class, color='red')
plt.xlabel('al')
plt.ylabel('household')
plt.show()
 
glass['household_pred_prob'] = logreg.predict_proba(X)[:, 1]
#绘图 绘制预测概率
 
plt.scatter(glass.al, glass.household)
plt.plot(glass.al, glass.household_pred_prob, color='red')
plt.xlabel('al')
plt.ylabel('household')
plt.show()
 
#检查一些例子的预测
print (logreg.predict_proba (1))
print (logreg.predict_proba(2))
print (logreg. predict_proba (3))
