# coding=utf-8
# By：Eastmount CSDN
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 
from matplotlib import axes
 
def draw_heatmap(data,xlabels,ylabels):
    #cmap=cm.Blues    
    cmap=cm.get_cmap('rainbow',1000)
    figure=plt.figure(facecolor='w')
    ax=figure.add_subplot(1,1,1,position=[0.1,0.15,0.8,0.8])
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax=data[0][0]
    vmin=data[0][0]
    for i in data:
        for j in i:
            if j>vmax:
                vmax=j
            if j<vmin:
                vmin=j
    map=ax.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=vmin,vmax=vmax)
    cb=plt.colorbar(mappable=map,cax=None,ax=None,shrink=0.5)
    plt.show()
            
a=np.random.rand(10,10)
print(a)
xlabels=['A','B','C','D','E','F','G','H','I','J']
ylabels=['a','b','c','d','e','f','g','h','i','j']
draw_heatmap(a,xlabels,ylabels)  
