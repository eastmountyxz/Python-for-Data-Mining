#coding=utf-8  
from matplotlib import pyplot as plt  
  
X = [[0, 0.25], [0.5, 0.75]]   
 
 
fig = plt.figure()
ax = fig.add_subplot(121)
im = ax.imshow(X, cmap=plt.get_cmap('hot'))
plt.colorbar(im, shrink=0.5)
 
ax = fig.add_subplot(122)
im = ax.imshow(X, cmap=plt.get_cmap('hot'), interpolation='nearest',
               vmin=0, vmax=1) 
plt.colorbar(im, shrink=0.2)
plt.show()
 
