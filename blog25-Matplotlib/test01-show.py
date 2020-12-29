#-*- coding:utf-8 -*-
import os
import codecs
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
 
x = [2.3, 4.5, 3, 7, 6.5, 4, 5.3]
y = [5, 4, 7, 5, 5.3, 5.5, 6.2]
 
num = np.arange(7)
name = ["a", "b", "c", "d", "e", "f", "g"]
 
fig, ax = plt.subplots()
ax.scatter(x,y,c='r',s=100)
 
for i,txt in enumerate(name):  #n  
    ax.annotate(txt,(x[i],y[i]))
 
plt.show()
