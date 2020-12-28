#coding: utf-8
import pandas as pd

#第一步 读取数据
f = open('data.csv',encoding='utf-8')
df = pd.read_csv(f)
print(df.shape)         #查看数据维度
print(df.head())        #查看前几行数据

#第二步 中文分词
import jieba
import jieba.posseg as psg

#格式转换 否则会报错  'float' object has no attribute 'decode'
df = pd.DataFrame(df['comment'].astype(str))

def chinese_word_cut(mytext):
    return ' '.join(jieba.cut(mytext))

#增加一列数据
df['content_cutted'] = df['comment'].apply(chinese_word_cut)
print(df.content_cutted.head())
