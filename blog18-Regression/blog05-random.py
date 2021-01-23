import numpy as np
import math
X = np.arange(0,50,0.2) 
print(X)
xArr = []
yArr = []
for n in X:
    xArr.append(n)
    y = 0.7*n + np.random.uniform(0,1)*math.sin(n)*2 - 3
    yArr.append(y)
 
import matplotlib.pyplot as plt
plt.plot(X, yArr, 'go')
plt.show()
