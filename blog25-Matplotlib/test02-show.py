#-*- coding:utf-8 -*-
import os
import codecs
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
 
x = [2.3, 4.5, 3, 7, 6.5, 4, 5.3]
y = [5, 4, 7, 5, 5.3, 5.5, 6.2]
 
n=np.arange(7)
name = ["a", "b", "c", "d", "e", "f", "g"]
 
fig, ax = plt.subplots()
ax.scatter(x,y,c='r',s=100)
 
#定义数组读取名称
corpus = []
result = codecs.open('allname.txt', 'r', 'utf-8')
for u in result.readlines():
    print(u.strip())
    corpus.append(u.strip())
 
#解决中文和负号'-'显示为方块的问题  
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False
 
for i,txt in enumerate(corpus): #n  name  
    ax.annotate(txt,(x[i],y[i]))
 
result.close()
plt.savefig('plot.png', dpi=1200)
plt.show()
