#encoding=utf-8
#By：Eastmount CSDN
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd  
 
#自定义函数 e指数形式
def func(x, a, b):
    return a*pow(x,b)
 
#导入数据及x、y散点坐标
data = pd.read_csv("data.csv")
print(data)
print(data.shape)    
print(data.head(5)) #显示前5行数据
x = data['x']
y = data['y']
print(x)
print(y)
 
#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数
a = popt[0] 
b = popt[1]
yvals = func(x,a,b) #拟合y值
print('系数a:', a)
print('系数b:', b)
 
#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.savefig('test3.png')
plt.show()
 
