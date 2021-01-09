# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import jieba
 
data = pd.read_csv("data.csv",encoding='gbk')
print(data)
 
#取表中的第1列的所有值
print("获取第一列内容")
col = data.iloc[:,0]  
#取表中所有值  
arrs = col.values
#去除停用词  
stopwords = {}.fromkeys(['，', '。', '！', '这', '我', '非常'])
 
print("\n中文分词后结果:")
corpus = []
for a in arrs:
    #print a
    seglist = jieba.cut(a,cut_all=False)     #精确模式  
    final = ''
    for seg in seglist:
        if seg not in stopwords: #不是停用词的保留
            final += seg
    seg_list = jieba.cut(final, cut_all=False) 
    output = ' '.join(list(seg_list))         #空格拼接
    print(output)
    corpus.append(output)
 
#计算词频
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
  
vectorizer = CountVectorizer() #将文本中的词语转换为词频矩阵  
X = vectorizer.fit_transform(corpus) #计算个词语出现的次数    
word = vectorizer.get_feature_names() #获取词袋中所有文本关键词  
for w in word: #查看词频结果
    print(w,)
print(X.toarray())  
