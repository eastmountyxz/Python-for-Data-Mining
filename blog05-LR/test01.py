# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 02:37:05 2016
@author: yxz15
"""
 
from sklearn import datasets
diabetes = datasets.load_diabetes()                          #载入数据
print(diabetes.data)                                         #数据
print(diabetes.target)                                       #类标
print('总行数: ', len(diabetes.data), len(diabetes.target))  #数据总行数
print('特征数: ', len(diabetes.data[0]))                     #每行数据集维数
print('数据类型: ', diabetes.data.shape)                     #类型
print(type(diabetes.data), type(diabetes.target))            #数据集类型
 
"""
[[ 0.03807591  0.05068012  0.06169621 ..., -0.00259226  0.01990842
  -0.01764613]
 [-0.00188202 -0.04464164 -0.05147406 ..., -0.03949338 -0.06832974
  -0.09220405]
  ...
 [-0.04547248 -0.04464164 -0.0730303  ..., -0.03949338 -0.00421986
   0.00306441]]
[ 151.   75.  141.  206.  135.   97.  138.   63.  110.  310.  101.
  ...
64.   48.  178.  104.  132.  220.   57.]
总行数:  442 442
特征数:  10
数据类型:  (442L, 10L)
<type 'numpy.ndarray'> <type 'numpy.ndarray'>
"""
