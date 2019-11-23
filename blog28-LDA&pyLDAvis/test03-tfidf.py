#coding: utf-8
import pandas as pd

#第一步 读取数据
f = open('data.csv')
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
print df.content_cutted.head()

#第三步 计算TF-IDF值
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

#设置特征数
n_features = 2000

tf_vectorizer = TfidfVectorizer(strip_accents = 'unicode',
                                max_features=n_features,
                                stop_words=['的','或','等','是','有','之','与','可以','还是','比较','这里',
                                            '一个','和','也','被','吗','于','中','最','但是','图片','大家',
                                            '一下','几天','200','还有','一看','300','50','哈哈哈哈',
                                             '“','”','。','，','？','、','；','怎么','本来','发现',
                                             'and','in','of','the','我们','一直','真的','18','一次',
                                           '了','有些','已经','不是','这么','一一','一天','这个','这种',
                                           '一种','位于','之一','天空','没有','很多','有点','什么','五个',
                                           '特别'],
                                max_df = 0.99,
                                min_df = 0.002) #去除文档内出现几率过大或过小的词汇
tf = tf_vectorizer.fit_transform(df.content_cutted)

print(tf.shape)
print(tf)
