# coding=utf-8
'''
' 这篇代码主要讲述获取MySQL中数据，再进行简单的统计
' 统计采用SQL语句进行 By:Eastmount CSDN
'''
 
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import pylab
import MySQLdb
from pylab import *
 
 
# 根据SQL语句输出24小时的柱状图
try:
    conn = MySQLdb.connect(host='localhost',user='root',
                         passwd='123456',port=3306, db='test01')
    cur = conn.cursor() #数据库游标
 
    #防止报错:UnicodeEncodeError: 'latin-1' codec can't encode character
    conn.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    sql = '''select DATE_FORMAT(FBTime,'%Y-%m-%d'), Count(*) from csdn
                group by DATE_FORMAT(FBTime,'%Y-%m-%d');'''
    cur.execute(sql)
    result = cur.fetchall()        #获取结果复合纸给result
    day1 = [n[0] for n in result]
    print len(day1)
    num1 = [n[1] for n in result]
    print len(num1),type(num1)
    matplotlib.style.use('ggplot')
    #获取第一天
    start = min(day1)
    print start
    #np.random.randn(len(num1)) 生成正确图形 正态分布随机数
    ts = pd.Series(np.random.randn(len(num1)),
                   index=pd.date_range(start, periods=len(num1)))
    ts = ts.cumsum()
    ts.plot()
    plt.title('Number-365Day')    
    plt.xlabel('Time')
    plt.ylabel('The number of blog')
    plt.savefig('04csdn.png',dpi=400)    
    plt.show()
 
 
#异常处理
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()  
    conn.close()
            
