# -*- coding: cp936 -*-
import pandas as pd
import numpy as np
 
a = np.random.standard_normal((9,4))
print(a.round(6)) #6位小数
print(a)

df = pd.DataFrame(a)
df.columns = ["No1", "No2", "No3", "No4"]
print(df)

dates = pd.date_range('2015-1-1',periods=9,freq='M')
print(dates)
df.index = dates
print(df)
