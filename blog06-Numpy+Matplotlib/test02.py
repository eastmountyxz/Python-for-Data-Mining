#定义二维数组
import numpy as np
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
 
#获取值
print('形状:', c.shape)
print('获取值:', c[1][0])
print('获取某行:')
print(c[1][:])
print('获取某行并切片:')
print(c[0][:-1])
print(c[0][-1:])
 
#获取具体某列值
print('获取第3列:')
print(c[:,np.newaxis, 2])
 
#调用sin函数
print(np.sin(np.pi/6))
print(type(np.sin(0.5)))
 
#范围定义
print(np.arange(0,4))
print(type(np.arange(0,4)))
