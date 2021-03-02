#encoding=utf-8  
import numpy as np
import matplotlib.pyplot as plt
 
#定义x、y散点坐标
x = np.arange(1, 16, 1)
num = [4.00, 5.20, 5.900, 6.80, 7.34,
       8.57, 9.86, 10.12, 12.56, 14.32,
       15.42, 16.50, 18.92, 19.58, 20.00]
y = np.array(num)
 
#用3次多项式拟合
f1 = np.polyfit(x, y, 3)
p1 = np.poly1d(f1)
print(p1)
 
#也可使用yvals=np.polyval(f1, x)
yvals = p1(x)  #拟合y值
 
#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()
plt.savefig('test.png')
