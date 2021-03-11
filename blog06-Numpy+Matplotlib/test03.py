#读取数据 header设置Excel无标题头
import pandas as pd
data = pd.read_excel("data.xls", header=None) 
print(data)
 
#计算数据长度
print('行数', len(data))
 
#计算用户A\B\C用电总和
print(data.sum())
 
#计算用户A\B\C用点量算术平均数
mm = data.sum()
print(mm)
 
#输出预览前5行数据
print('预览前5行数据')
print(data.head())
 
#输出数据基本统计量
print('输出数据基本统计量')
print(data.describe())
