from pandas import Series, DataFrame
 
#通过传递一个list对象来创建Series，默认创建整型索引；
a = Series([4, 7, -5, 3])
print('创建Series:')
print(a)
 
#创建一个带有索引来确定每一个数据点的Series ;
b = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print('创建带有索引的Series:')
print(b)
 
#如果你有一些数据在一个Python字典中，你可以通过传递字典来创建一个Series；
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
c = Series(sdata)
print('通过传递字典创建Series:')
print(c)
states = ['California', 'Ohio', 'Oregon', 'Texas']
d = Series(sdata, index=states)
print('California没有字典为空:')
print(d)
