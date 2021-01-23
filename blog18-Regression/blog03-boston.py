# -*- coding: utf-8 -*-
#导入数据集boston
from sklearn.datasets import load_boston
import numpy as np
boston = load_boston()
print(boston.data.shape, boston.target.shape)
print(boston.data[0])
print(boston.target)

#划分数据集
boston_temp = boston.data[:, np.newaxis, 5]   
x_train = boston_temp[:-100]      #训练样本  
x_test = boston_temp[-100:]       #测试样本 后100行  
y_train = boston.target[:-100]    #训练标记  
y_test = boston.target[-100:]     #预测对比标记
