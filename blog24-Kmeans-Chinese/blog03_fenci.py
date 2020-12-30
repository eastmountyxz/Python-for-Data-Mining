#encoding=utf-8
import sys
import re
import codecs
import os
import shutil
import jieba
import jieba.analyse
 
#导入自定义词典
#jieba.load_userdict("dict_baidu.txt")
 
#Read file and cut
def read_file_cut():
 
    fileName = "HudongSpider_Result.txt"
    source = open(fileName, 'r', encoding='utf8')
    resName = "Stop_HudongSpider_Result.txt"
    result = codecs.open(resName, 'w', 'utf-8')
    line = source.readline()
        
    while line!="":
        seglist = jieba.cut(line,cut_all=False)  #精确模式
        output = ' '.join(list(seglist))         #空格拼接
        #print output
        result.write(output)
        line = source.readline()
    else:
        source.close()
        result.close()
        print('End All')
 
#Run function
if __name__ == '__main__':
    read_file_cut()
