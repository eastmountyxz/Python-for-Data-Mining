# coding=utf-8            
import re          
import os  
import sys
import codecs
import shutil
 
def merge_file():
    path = "BaiduSpiderSpots\\"
    resName = "BaiduSpider_Result.txt"
    if os.path.exists(resName):
        os.remove(resName)
    result = codecs.open(resName, 'w', 'utf-8')
 
    num = 1
    while num <= 100:
        name = "%04d" % num 
        fileName = path + str(name) + ".txt"
        source = open(fileName, 'r', encoding='utf-8')
        line = source.readline()
        line = line.strip('\n')
        line = line.strip('\r')
 
        while line!="":
            line = line.replace('\n',' ')
            line = line.replace('\r',' ')
            result.write(line+ ' ')
            line = source.readline()
        else:
            print('End file: ' + str(num))
            result.write('\r\n')
            source.close()
        num = num + 1
        
    else:
        print('End All')
        result.close()    
 
if __name__ == '__main__':
    merge_file()
