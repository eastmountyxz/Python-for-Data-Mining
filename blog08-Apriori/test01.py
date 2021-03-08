# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 03:29:51 2016
地址：http://blog.csdn.net/u010454729/article/details/49078505
@author: 参考CSDN u010454729 
"""

def loadDataSet():  
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]  
  
def createC1(dataSet):                  #构建所有候选项集的集合  
    C1 = []  
    for transaction in dataSet:  
        for item in transaction:  
            if not [item] in C1:  
                C1.append([item])       #C1添加的是列表，对于每一项进行添加，{1},{3},{4},{2},{5}  
    C1.sort()  
    return map(frozenset, C1)           #使用frozenset，被“冰冻”的集合，为后续建立字典key-value使用。  
  
def scanD(D,Ck,minSupport):             #由候选项集生成符合最小支持度的项集L。参数分别为数据集、候选项集列表，最小支持度  
    ssCnt = {}  
    for tid in D:                       #对于数据集里的每一条记录  
        for can in Ck:                  #每个候选项集can  
            if can.issubset(tid):       #若是候选集can是作为记录的子集，那么其值+1,对其计数  
                if can not in ssCnt:    #ssCnt[can] = ssCnt.get(can,0)+1一句可破，没有的时候为0,加上1,有的时候用get取出，加1  
                    ssCnt[can] = 1  
                else:  
                    ssCnt[can] += 1
    numItems = float(len(list(D)))    
    retList  = []  
    supportData = {}  
    for key in ssCnt:
        if numItems > 0:                #除以总的记录条数，即为其支持度
            support = ssCnt[key] / numItems
        else:
            support = 0
        if support >= minSupport:  
            retList.insert(0,key)       #超过最小支持度的项集，将其记录下来。  
        supportData[key] = support  
    return retList, supportData
  
def aprioriGen(Lk, k):                  #创建符合置信度的项集Ck,  
    retList = []  
    lenLk   = len(Lk)  
    for i in range(lenLk):  
        for j in range(i+1, lenLk):     #k=3时，[:k-2]即取[0],对{0,1},{0,2},{1,2}这三个项集来说，L1=0，L2=0，将其合并得{0,1,2}，当L1=0,L2=1不添加，  
            L1 = list(Lk[i])[:k-2]  
            L2 = list(Lk[j])[:k-2]  
            L1.sort()  
            L2.sort()  
            if L1==L2:  
                retList.append(Lk[i]|Lk[j])  
    return retList  
  
def apriori(dataSet, minSupport = 0.5):  
    C1 = createC1(dataSet)  
    D  = map(set,dataSet)  
    L1, supportData = scanD(D,C1,minSupport)  
    L  = [L1]                           #L将包含满足最小支持度，即经过筛选的所有频繁n项集，这里添加频繁1项集  
    k  = 2  
    while (len(L[k-2])>0):              #k=2开始，由频繁1项集生成频繁2项集，直到下一个打的项集为空  
        Ck = aprioriGen(L[k-2], k)  
        Lk, supK = scanD(D, Ck, minSupport)  
        supportData.update(supK)        #supportData为字典，存放每个项集的支持度，并以更新的方式加入新的supK  
        L.append(Lk)  
        k +=1  
    return L,supportData  
  
dataSet = loadDataSet()  
C1 = createC1(dataSet)

print("所有候选1项集C1:\n")
for n in C1:
 print(n)
  
D = map(set, dataSet)  
print("数据集D:\n")
for n in D:
    print(n)
  
L1, supportData0 = scanD(D,C1, 0.5)  
print("符合最小支持度的频繁1项集L1:\n",L1)
  
L, suppData = apriori(dataSet)  
print("所有符合最小支持度的项集L：\n",L)
print("频繁2项集：\n",aprioriGen(L[0],2))

L, suppData = apriori(dataSet, minSupport=0.7)  
print("所有符合最小支持度为0.7的项集L：\n",L)

