#coding: utf-8
import pandas as pd

#读取数据
f = open('data.csv',encoding='utf-8')
df = pd.read_csv(f)
print(df.shape)         #查看数据维度
print(df.head())        #查看前几行数据
