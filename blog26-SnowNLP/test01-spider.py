# coding=utf-8  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import selenium.webdriver.support.ui as ui  
from selenium.webdriver.common.action_chains import ActionChains  
import time      
import re      
import os
import csv
import codecs

#写入文件
c = open("test-douban.csv", "wb")  #写文件
c.write(codecs.BOM_UTF8)          #防止乱码
writer = csv.writer(c)                     #写入对象
writer.writerow(['序号','用户名','链接','评分','评分标题','有用数','日期','评论'])

#打开Firefox浏览器 设定等待加载时间 访问URL  
driver = webdriver.Firefox()
i = 0
while i<10:
    num = i*20
    url = "https://movie.douban.com/subject/1292052/comments?start=" + str(num) +"&limit=20&sort=new_score&status=P"
    print(url)
    driver.get(url)
    #用户姓名 超链接
    elem1 = driver.find_elements_by_xpath("//div[@class='avatar']/a")     
    #用户评分
    elem2 = driver.find_elements_by_xpath("//span[@class='comment-info']/span[2]")
    #有用数
    elem3 = driver.find_elements_by_xpath("//span[@class='comment-vote']/span[1]")
    #日期
    elem4 = driver.find_elements_by_xpath("//span[@class='comment-time ']")
    #评论
    elem5 = driver.find_elements_by_xpath("//span[@class='short']")

    #循环写入20行评价
    tlist = []
    k = 0
    while k<20:
        #序号
        num = i*20+k+1
        print(num)
        #用户姓名
        name = elem1[k].get_attribute("title").encode('utf-8')
        print(name)
        #超链接
        href = elem1[k].get_attribute("href").encode('utf-8')
        print(href)
        #用户评分及内容
        score = elem2[k].get_attribute("class").encode('utf-8')
        print(score)
        content = elem2[k].get_attribute("title").encode('utf-8')
        print(content)
        #有用数
        useful = elem3[k].text.encode('utf-8')
        print(useful)
        #日期
        date = elem4[k].text.encode('utf-8')
        #评论
        shortcon = elem5[k].text.encode('utf-8')
        print(shortcon)

        #写入文件
        templist = []
        templist.append(num)
        templist.append(name)
        templist.append(href)
        templist.append(score)
        templist.append(content)
        templist.append(useful)
        templist.append(date)
        templist.append(shortcon)
        writer.writerow(templist)
        
        k = k + 1
            
    i = i + 1

c.close()
