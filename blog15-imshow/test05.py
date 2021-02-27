#coding=utf-8  
from matplotlib import pyplot as plt  
  
X = [[1,2],[3,4]]   
 
fig = plt.figure()
ax = fig.add_subplot(231)
ax.imshow(X)
 
ax = fig.add_subplot(232)
ax.imshow(X, cmap=plt.cm.gray) #灰度
 
ax = fig.add_subplot(233)
im = ax.imshow(X, cmap=plt.cm.spring) #春
plt.colorbar(im)                
 
ax = fig.add_subplot(234)
im = ax.imshow(X, cmap=plt.cm.summer)
plt.colorbar(im, cax=None, ax=None, shrink=0.5) #长度为半
 
ax = fig.add_subplot(235)
im = ax.imshow(X, cmap=plt.cm.autumn)
plt.colorbar(im, shrink=0.5, ticks=[-1,0,1])
 
ax = fig.add_subplot(236)
im = ax.imshow(X, cmap=plt.cm.winter)
plt.colorbar(im, shrink=0.5)
 
plt.show()
