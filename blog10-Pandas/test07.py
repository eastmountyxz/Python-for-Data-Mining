# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 21:47:46 2017
@author: yxz
"""
 
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------
#载入数据
def loadDataSet(fileName,delim='\t'):
    fr=open(fileName)
    stringArr=[line.strip().split(delim) for line in fr.readlines()]
    datArr=[list(map(float,line)) for line in stringArr]
    return mat(datArr)
 
def pca(dataMat,topNfeat=9999999):
    meanVals=mean(dataMat,axis=0)
    meanRemoved=dataMat-meanVals
    covMat=cov(meanRemoved,rowvar=0)
    eigVals,eigVets=linalg.eig(mat(covMat))
    eigValInd=argsort(eigVals)
    eigValInd=eigValInd[:-(topNfeat+1):-1]
    redEigVects=eigVets[:,eigValInd]
    print(meanRemoved)
    print(redEigVects)
    lowDDatMat=meanRemoved*redEigVects
    reconMat=(lowDDatMat*redEigVects.T)+meanVals
    return lowDDatMat,reconMat

dataMat=loadDataSet('41.txt')
lowDMat,reconMat=pca(dataMat,1)

#-----------------------------------------------------------------------
#绘制图像 
def plotPCA(dataMat,reconMat):
    datArr=array(dataMat)
    reconArr=array(reconMat)
    n1=shape(datArr)[0]
    n2=shape(reconArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n1):
        xcord1.append(datArr[i,0])
        ycord1.append(datArr[i,1])
    for i in range(n2):
        xcord2.append(reconArr[i,0])
        ycord2.append(reconArr[i,1])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=90,c='red',marker='^')
    ax.scatter(xcord2,ycord2,s=50,c='yellow',marker='o')
    plt.title('PCA')
    plt.savefig('ccc.png',dpi=400)
    plt.show()

plotPCA(dataMat,reconMat)
