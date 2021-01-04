# -*- coding: cp936 -*-
import pandas as pd
import numpy as np
 
a = np.random.standard_normal((9,4))
df = pd.DataFrame(a)
df.columns = ["No1", "No2", "No3", "No4"]
dates = pd.date_range('2015-1-1',periods=9,freq='M')
df.index = dates
 
df['Quarter'] = ['Q1','Q1','Q1','Q2','Q2','Q2','Q3','Q3','Q3']
print(df)
groups = df.groupby('Quarter')
print(groups.sum())
print(groups.mean())
print(groups.max())
print(groups.size())
