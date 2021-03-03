# coding=utf-8
'''
' 这篇代码主要讲述获取MySQL中数据，再进行简单的统计
' 统计采用SQL语句进行 By:Eastmount CSDN 杨秀璋
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
    sql = '''select  
            COUNT(case dayofweek(FBTime)  when 1 then 1 end) AS '星期日',
            COUNT(case dayofweek(FBTime)  when 2 then 1 end) AS '星期一',
            COUNT(case dayofweek(FBTime)  when 3 then 1 end) AS '星期二',
            COUNT(case dayofweek(FBTime)  when 4 then 1 end) AS '星期三',
            COUNT(case dayofweek(FBTime)  when 5 then 1 end) AS '星期四',
            COUNT(case dayofweek(FBTime)  when 6 then 1 end) AS '星期五',
            COUNT(case dayofweek(FBTime)  when 7 then 1 end) AS '星期六'
            from csdn_blog where DATE_FORMAT(FBTime,'%Y')='2008';
          '''
    cur.execute(sql)
    result1 = cur.fetchall()        
    print result1
    name = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    data = np.array(result1)
    d1 = data.T #转置
    print d1
 
 
    sql = '''select  
            COUNT(case dayofweek(FBTime)  when 1 then 1 end) AS '星期日',
            COUNT(case dayofweek(FBTime)  when 2 then 1 end) AS '星期一',
            COUNT(case dayofweek(FBTime)  when 3 then 1 end) AS '星期二',
            COUNT(case dayofweek(FBTime)  when 4 then 1 end) AS '星期三',
            COUNT(case dayofweek(FBTime)  when 5 then 1 end) AS '星期四',
            COUNT(case dayofweek(FBTime)  when 6 then 1 end) AS '星期五',
            COUNT(case dayofweek(FBTime)  when 7 then 1 end) AS '星期六'
            from csdn_blog where DATE_FORMAT(FBTime,'%Y')='2011';
          '''
    cur.execute(sql)
    result2 = cur.fetchall()        
    data = np.array(result2)
    d2 = data.T #转置
    print d2
 
 
    sql = '''select  
            COUNT(case dayofweek(FBTime)  when 1 then 1 end) AS '星期日',
            COUNT(case dayofweek(FBTime)  when 2 then 1 end) AS '星期一',
            COUNT(case dayofweek(FBTime)  when 3 then 1 end) AS '星期二',
            COUNT(case dayofweek(FBTime)  when 4 then 1 end) AS '星期三',
            COUNT(case dayofweek(FBTime)  when 5 then 1 end) AS '星期四',
            COUNT(case dayofweek(FBTime)  when 6 then 1 end) AS '星期五',
            COUNT(case dayofweek(FBTime)  when 7 then 1 end) AS '星期六'
            from csdn_blog where DATE_FORMAT(FBTime,'%Y')='2016';
          '''
    cur.execute(sql)
    result3 = cur.fetchall()       
    data = np.array(result3)
    print type(result3),type(data)
    d3 = data.T #转置
    print d3
 
 
    #SQL语句获取3个数组，采用循环复制到一个[7][3]的二维数组中
    data = np.random.rand(7,3)
    print data
    i = 0
    while i<7:
        data[i][0] = d1[i]
        data[i][1] = d2[i]
        data[i][2] = d3[i]
        i = i + 1
 
    print data
    print type(data)
 
    #绘图
    matplotlib.style.use('ggplot')
    #数据[7,3]数组 name为星期 columns对应年份
    df=DataFrame(data, index=name, columns=['2008','2011','2016'])
    df.plot(kind='bar')   
    plt.title('Comparison Chart Blog-Week')    
    plt.xlabel('Week')
    plt.ylabel('The number of blog')
    plt.savefig('03csdn.png', dpi=400)
    plt.show()
 
 
 
#异常处理
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()  
    conn.close()
      
