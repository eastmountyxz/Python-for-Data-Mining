# coding=utf-8
'''
' 这篇代码主要讲述获取MySQL中数据，再进行简单的统计
' 统计采用SQL语句进行
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
    
 
    #################################################
    # 2014年
    #################################################
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog
            where DATE_FORMAT(FBTime,'%Y')='2014' group by mm;'''
    cur.execute(sql)
    result = cur.fetchall() #获取结果复制给result
    hour1 = [n[0] for n in result]
    print hour1
    num1 = [n[1] for n in result]
    print num1
 
    N =  12
    ind = np.arange(N)  #赋值0-11  
    width=0.35
    p1 = plt.subplot(221)
    plt.bar(ind, num1, width, color='b', label='sum num')   
    #设置底部名称    
    plt.xticks(ind+width/2, hour1, rotation=40) #旋转40度
    for i in range(12):   #中心底部翻转90度
        plt.text(i, num1[i], str(num1[i]),
                 ha='center', va='bottom', rotation=45) 
    plt.title('2014 Number-12Month')    
    plt.sca(p1)
 
 
    #################################################
    # 2015年
    #################################################
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog
            where DATE_FORMAT(FBTime,'%Y')='2015' group by mm;'''
    cur.execute(sql)
    result = cur.fetchall()        
    hour1 = [n[0] for n in result]
    print hour1
    num1 = [n[1] for n in result]
    print num1
    
    N =  12
    ind = np.arange(N)  #赋值0-11  
    width=0.35
    p2 = plt.subplot(222)
    plt.bar(ind, num1, width, color='r', label='sum num')   
    #设置底部名称    
    plt.xticks(ind+width/2, hour1, rotation=40) #旋转40度
    for i in range(12):   #中心底部翻转90度
        plt.text(i, num1[i], str(num1[i]),
                 ha='center', va='bottom', rotation=45) 
    plt.title('2015 Number-12Month')    
    plt.sca(p2)
 
 
    #################################################
    # 2016年
    #################################################
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog
            where DATE_FORMAT(FBTime,'%Y')='2016' group by mm;'''
    cur.execute(sql)
    result = cur.fetchall()        
    hour1 = [n[0] for n in result]
    print hour1
    num1 = [n[1] for n in result]
    print num1
 
    N =  12
    ind = np.arange(N)  #赋值0-11 
    width=0.35
    p3 = plt.subplot(223)
    plt.bar(ind, num1, width, color='g', label='sum num')   
    #设置底部名称    
    plt.xticks(ind+width/2, hour1, rotation=40) #旋转40度
    for i in range(12):   #中心底部翻转90度
        plt.text(i, num1[i], str(num1[i]),
                 ha='center', va='bottom', rotation=45) 
    plt.title('2016 Number-12Month')    
    plt.sca(p3)
 
    
    #################################################
    # 所有年份数据对比
    #################################################
    sql = '''select MONTH(FBTime) as mm, count(*) as cnt from csdn_blog group by mm;'''
    cur.execute(sql)
    result = cur.fetchall()     
    hour1 = [n[0] for n in result]
    print hour1
    num1 = [n[1] for n in result]
    print num1
 
    N =  12
    ind = np.arange(N)  #赋值0-11  
    width=0.35
    p4 = plt.subplot(224)
    plt.bar(ind, num1, width, color='y', label='sum num')   
    #设置底部名称    
    plt.xticks(ind+width/2, hour1, rotation=40) #旋转40度
    for i in range(12):   #中心底部翻转90度
        plt.text(i, num1[i], str(num1[i]),
                 ha='center', va='bottom', rotation=45) 
    plt.title('All Year Number-12Month')    
    plt.sca(p4)
 
    plt.savefig('ttt.png',dpi=400)    
    plt.show()
 
#异常处理
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()  
    conn.close()
 
 
