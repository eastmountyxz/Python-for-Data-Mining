# coding=utf-8  
import time          
import re          
import os  
import sys
import codecs
import shutil
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer 
 
if __name__ == "__main__":
    
    #########################################################################
    #                           第一步 计算TFIDF
    
    #文档预料 空格连接
    corpus = []
    
    #读取预料 一行预料为一个文档
    for line in open('Stop_HudongSpider_Result.txt', 'r', encoding='utf8').readlines():
        #print line
        corpus.append(line.strip())
    
    #将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    #remove words occuring less than 5 times
    vectorizer = CountVectorizer(min_df=2)
    print(type(vectorizer))
 
    #该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
 
    #第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    print(type(tfidf))
 
    #获取词袋模型中的所有词语  
    word = vectorizer.get_feature_names()
    
    #将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    X = tfidf.toarray()
    weight = np.array(X, dtype='float32')
    print(type(weight))
    print(weight.shape)

    #MemoryError: Unable to allocate array with shape (400, 143556) and data type float64
    #remove words occuring less than 5 times
    
    #打印特征向量文本内容
    print('Features length: ' + str(len(word)))
    
    """
    resName = "BHTfidf_Result.txt"
    result = codecs.open(resName, 'w', 'utf-8')
    for j in range(len(word)):
        result.write(word[j] + ' ')
    result.write('\r\n\r\n')
 
    #打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
    for i in range(len(weight)):
        #print u"-------这里输出第", i, u"类文本的词语tf-idf权重------"  
        for j in range(len(word)):
            #print weight[i][j],
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')
 
    result.close()
    """
 
 
    ########################################################################
    #                               第二步 聚类Kmeans
 
    print('Start Kmeans:')
    from sklearn.cluster import KMeans
    clf = KMeans(n_clusters=4)   #景区 动物 人物 国家
    s = clf.fit(weight)
    print(s)
 
    '''
    print 'Start MiniBatchKmeans:'
    from sklearn.cluster import MiniBatchKMeans
    clf = MiniBatchKMeans(n_clusters=20)
    s = clf.fit(weight)
    print s
    '''
 
    #中心点
    print(clf.cluster_centers_)
    
    #每个样本所属的簇
    label = []               #存储400个类标 
    print(clf.labels_)
    i = 1
    while i <= len(clf.labels_):
        #print(clf.labels_[i-1])
        label.append(clf.labels_[i-1])
        i = i + 1
 
    #用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数  958.137281791
    print(clf.inertia_)
    y_pred = clf.labels_
    
 
 
    ########################################################################
    #                               第三步 图形输出 降维
 
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)             #输出两维
    newData = pca.fit_transform(weight)   #载入N维
    print(newData)
 
    x = [n[0] for n in newData]
    y = [n[1] for n in newData]
 
    x1, y1 = [], []   
    x2, y2 = [], [] 
    x3, y3 = [], []
    x4, y4 = [], []
    
    #分布获取类标为0、1、2、3的数据 赋值给(x1,y1) (x2,y2) (x3,y3) (x4,y4)
    i = 0  
    while i < len(newData):  
        if y_pred[i]==0:  
            x1.append(newData[i][0])  
            y1.append(newData[i][1])  
        elif y_pred[i]==1:  
            x2.append(newData[i][0])  
            y2.append(newData[i][1])  
        elif y_pred[i]==2:  
            x3.append(newData[i][0])  
            y3.append(newData[i][1])
        elif y_pred[i]==3:  
            x4.append(newData[i][0])  
            y4.append(newData[i][1])
        i = i + 1
        
    #四种颜色 红 绿 蓝，marker='x'表示类型，o表示圆点 *表示星型 x表示点   
    plot1, = plt.plot(x1, y1, 'or', marker="o", markersize=10)    
    plot2, = plt.plot(x2, y2, 'og', marker="o", markersize=10)    
    plot3, = plt.plot(x3, y3, 'ob', marker="o", markersize=10)
    plot4, = plt.plot(x4, y4, 'oy', marker="o", markersize=10)   
    #plt.title("K-Means Text Clustering")  #绘制标题
    plt.legend((plot1, plot2, plot3, plot4), ('A', 'B', 'C', 'D'), fontsize=10)  
 
    #四种颜色 红 绿 蓝 黑
    #plt.scatter(x1, x2, c=clf.labels_,  s=100)
    plt.show()
 
