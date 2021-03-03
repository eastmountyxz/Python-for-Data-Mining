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
    sql = '''select  
            COUNT(case dayofweek(FBTime)  when 1 then 1 end) AS '星期日',
            COUNT(case dayofweek(FBTime)  when 2 then 1 end) AS '星期一',
            COUNT(case dayofweek(FBTime)  when 3 then 1 end) AS '星期二',
            COUNT(case dayofweek(FBTime)  when 4 then 1 end) AS '星期三',
            COUNT(case dayofweek(FBTime)  when 5 then 1 end) AS '星期四',
            COUNT(case dayofweek(FBTime)  when 6 then 1 end) AS '星期五',
            COUNT(case dayofweek(FBTime)  when 7 then 1 end) AS '星期六'
            from csdn_blog;
          '''
    cur.execute(sql)
    result = cur.fetchall()     
    print result
    #((31704L, 43081L, 42670L, 43550L, 41270L, 39164L, 29931L),)
    name = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    #转换为numpy数组
    data = np.array(result)
    print data
    d = data.T #转置
    print d
 
    matplotlib.style.use('ggplot')
    df=DataFrame(d, index=name,columns=['Nums'])
    df.plot(kind='bar')
    plt.title('All Year Blog-Week')    
    plt.xlabel('Week')
    plt.ylabel('The number of blog')
    plt.savefig('01csdn.png',dpi=400)
    plt.show()
 
#异常处理
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()  
    conn.close()
       
