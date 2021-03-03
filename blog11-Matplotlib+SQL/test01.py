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
    sql = "select HOUR(FBTime) as hh, count(*) as cnt from csdn group by hh;"
    cur.execute(sql)
    result = cur.fetchall()        #获取结果复合纸给result
    hour1 = [n[0] for n in result]
    print hour1
    num1 = [n[1] for n in result]
    print num1
    
    N = 23  
    ind = np.arange(N)  #赋值0-23  
    width=0.35  
    plt.bar(ind, num1, width, color='r', label='sum num')   
    #设置底部名称    
    plt.xticks(ind+width/2, hour1, rotation=40) #旋转40度
    for i in range(23):   #中心底部翻转90度
        plt.text(i, num1[i], str(num1[i]),
                 ha='center', va='bottom', rotation=45) 
    plt.title('Number-24Hour')    
    plt.xlabel('hours')
    plt.ylabel('The number of blog')
    plt.legend()
    plt.savefig('08csdn.png',dpi=400)    
    plt.show()
 
 
#异常处理
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()  
    conn.close()
 
       
