# coding=utf-8
'''
' 这篇代码主要讲述获取MySQL中数据，再进行简单的统计
' 统计采用SQL语句进行 By：Eastmount CSDN
'''
 
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import MySQLdb
from pandas import *
 
try:
    conn = MySQLdb.connect(host='localhost',user='root',
                         passwd='123456',port=3306, db='test01')
    cur = conn.cursor() #数据库游标
 
    #防止报错:UnicodeEncodeError: 'latin-1' codec can't encode character
    conn.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
 
    #所有博客数
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog
             group by mm;'''
    cur.execute(sql)
    result = cur.fetchall()        #获取结果复制给result
    hour1 = [n[0] for n in result]
    print hour1
    num1 = [n[1] for n in result]
    print num1
 
    #2014年博客数
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog
             where DATE_FORMAT(FBTime,'%Y')='2014' group by mm;'''
    cur.execute(sql)
    result = cur.fetchall()        
    num2 = [n[1] for n in result]
    print num2
 
    #2015年博客数
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog
             where DATE_FORMAT(FBTime,'%Y')='2015' group by mm;'''
    cur.execute(sql)
    result = cur.fetchall()       
    num3 = [n[1] for n in result]
    print num3
 
    #2016年博客数
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog
             where DATE_FORMAT(FBTime,'%Y')='2016' group by mm;'''
    cur.execute(sql)
    result = cur.fetchall()       
    num4 = [n[1] for n in result]
    print num4
 
    #重点: 数据整合 [12,4]
    data = np.array([num1, num2, num3, num4])
    print data
    d = data.T #转置
    print d
    df = DataFrame(d, index=hour1, columns=['All','2014', '2015', '2016'])
    df.plot(kind='area', alpha=0.2) #设置颜色 透明度
    plt.title('Arae Plot Blog-Month') 
    plt.savefig('csdn.png',dpi=400) 
    plt.show()
 
#异常处理
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()  
    conn.close()
    
