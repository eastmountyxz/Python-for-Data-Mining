# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
 
data = pd.read_csv("data.csv",encoding='gbk')
print(data)
 
#取表中的第1列的所有值
print("获取第一列内容")
col = data.iloc[:,0]  
#取表中所有值  
arrs = col.values
for a in arrs:
    print(a)
