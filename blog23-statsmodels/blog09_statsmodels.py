# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
 
dta=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422, 
6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355, 
10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767, 
12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232, 
13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248, 
9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722, 
11999,9390,13481,14795,15845,15271,14686,11054,10395]
 
dta = np.array(dta,dtype=np.float) 
df = pd.Series(dta)
print(df)
dates = pd.date_range('2001', periods=90, freq='A')
df.index = dates
print(df)
df.plot(figsize=(12,8))
 
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(111)
diff1 = df.diff(1)
diff1.plot(ax=ax1)
 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
f = plt.figure(facecolor='white')
ax1 = f.add_subplot(211)
plot_acf(df, lags=40, ax=ax1)
ax2 = f.add_subplot(212)
plot_pacf(df, lags=40, ax=ax2)
plt.show()
 
 
#预测结果
import statsmodels.api as sm
arma_mod80 =  sm.tsa.ARMA(df,(8,0)).fit()
print(arma_mod80.aic, arma_mod80.bic, arma_mod80.hqic)
 
pre = arma_mod80.predict('2090', '2100', dynamic=True)
print(pre)
 
fig, ax = plt.subplots(figsize=(12, 8))
ax = df.ix['2000':].plot(ax=ax)
fig = arma_mod80.plot_predict('2090', '2100', dynamic=True, ax=ax, plot_insample=False)
plt.show()
