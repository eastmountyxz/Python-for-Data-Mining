import numpy as np
import pylab as pl
# make an array of random numbers with a gaussian distribution with
# mean = 5.0
# rms = 3.0
# number of points = 1000
data = np.random.normal(5.0, 3.0, 1000)
# make a histogram of the data array
pl.hist(data, histtype='stepfilled') #去掉黑色轮廓
# make plot labels
pl.xlabel('data') 
pl.show()
