# coding=utf-8  
# test09_03.py                
import os  
import codecs
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys       
 
driver = webdriver.Firefox()

"""
该部分代码采用python2编写，并且产生于五年前
主要提供思路，建议大家结合现在的百科HTML节点进行分析和爬取
该资源更推荐大家运行其他预处理和分析部分的代码
祝好！

——BY: Eastmount
"""
 
#获取摘要信息
def getAbstract(name):  
    try:
        #新建文件夹及文件
        basePathDirectory = "Hudong_Coding"  
        if not os.path.exists(basePathDirectory):  
            os.makedirs(basePathDirectory)  
        baiduFile = os.path.join(basePathDirectory,"HudongSpider.txt")
        #文件不存在新建,存在则追加写入
        if not os.path.exists(baiduFile):  
            info = codecs.open(baiduFile,'w','utf-8')  
        else:  
            info = codecs.open(baiduFile,'a','utf-8')  
 
        url = "http://www.baike.com/wiki/" + name
        print url
        driver.get(url)  
        elem = driver.find_element_by_xpath("//div[@class='summary']/p")  
        print elem.text
        info.writelines(elem.text+'\r\n')  
          
    except Exception,e: 
        print "Error: ",e  
    finally:  
        print '\n'  
        info.write('\r\n')  
  
#主函数  
def main():
    languages = ["JavaScript", "Java", "Python", "Ruby", "PHP",
                 "C++", "CSS", "C#", "C", "GO"]
    print u'开始爬取'
    for lg in languages:  
        print lg
        getAbstract(lg)  
    print u'结束爬取'  
 
if __name__ == '__main__':
    main()  
