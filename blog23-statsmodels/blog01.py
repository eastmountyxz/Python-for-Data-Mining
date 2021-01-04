import pandas as pd
import numpy as np
 
df = pd.DataFrame([10,20,30,40],columns=['num'],
                  index=['a','b','c','d'])
 
print(df.index)
print(df.columns)
print(df.ix['c'])
print(df.ix[df.index[1:3]])
print(df.sum())
print(df.apply(lambda x:x**2))
