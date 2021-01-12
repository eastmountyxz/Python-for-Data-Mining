# -*- coding: utf-8 -*-
import os 
import numpy as np
data = np.loadtxt("wine.txt",dtype=str,delimiter=",")
print(data)
 
yy, x = np.split(data, (1,), axis=1)
print(yy.shape, x.shape)
print(x)
print(yy[:5])
