#coding:utf-8
import numpy as np
import pandas as pd
import csv

#全局变量
global x_mat

#数据标准化
def ZscoreNormalization(x, n):
    print(len(x))
    i = 0
    while i<len(x):
        x_mat[i][n] = (x[i] - np.mean(x)) / np.std(x)
        #if x_mat[i][n]>0:
        #    print(x_mat[i][n])
        i = i + 1
    print("The ", n , "feature  is normal.")

#-------------------------------------读取文件划分数据集-----------------------------------------
fr = open("kddcup.data_10_percent_corrected.csv")
data_file = open("kddcup.data_10_percent_corrected-result.csv",'wb+')
lines = fr.readlines()
line_nums = len(lines)
print(line_nums)

#创建line_nums行 para_num列的矩阵
x_mat = np.zeros((line_nums, 42))

#划分数据集
for i in range(line_nums):
    line = lines[i].strip()
    item_mat = line.split(',')
    x_mat[i, :] = item_mat[0:42]    #获取42个特征
fr.close()
print(x_mat.shape)

#--------------------------------获取某列特征并依次标准化并赋值-----------------------------
print(len(x_mat[:, 0])) #获取某列数据 494021
print(len(x_mat[0, :])) #获取某行数据 42

#标准化处理 
ZscoreNormalization(x_mat[:, 0], 0)    #duration
ZscoreNormalization(x_mat[:, 0], 4)    #src_bytes
ZscoreNormalization(x_mat[:, 0], 5)    #dst_bytes
ZscoreNormalization(x_mat[:, 0], 7)    #wrong_fragment
ZscoreNormalization(x_mat[:, 0], 8)    #urgent

ZscoreNormalization(x_mat[:, 0], 9)    #hot
ZscoreNormalization(x_mat[:, 0], 10)  #num_failed_logins
ZscoreNormalization(x_mat[:, 0], 12)  #num_compromised
ZscoreNormalization(x_mat[:, 0], 14)  #su_attempte
ZscoreNormalization(x_mat[:, 0], 15)  #num_root
ZscoreNormalization(x_mat[:, 0], 16)  #num_file_creations
ZscoreNormalization(x_mat[:, 0], 17)  #num_shells
ZscoreNormalization(x_mat[:, 0], 18)  #num_access_files
ZscoreNormalization(x_mat[:, 0], 19)  #num_outbound_cmds

ZscoreNormalization(x_mat[:, 0], 22)  #count
ZscoreNormalization(x_mat[:, 0], 23)  #srv_count
ZscoreNormalization(x_mat[:, 0], 24)  #serror_rate
ZscoreNormalization(x_mat[:, 0], 25)  #srv_serror_rate
ZscoreNormalization(x_mat[:, 0], 26)  #rerror_rate
ZscoreNormalization(x_mat[:, 0], 27)  #srv_rerror_rate
ZscoreNormalization(x_mat[:, 0], 28)  #same_srv_rate
ZscoreNormalization(x_mat[:, 0], 29)  #diff_srv_rate
ZscoreNormalization(x_mat[:, 0], 30)  #srv_diff_host_rate

ZscoreNormalization(x_mat[:, 0], 31)  #dst_host_count
ZscoreNormalization(x_mat[:, 0], 32)  #dst_host_srv_count
ZscoreNormalization(x_mat[:, 0], 33)  #dst_host_same_srv_rate
ZscoreNormalization(x_mat[:, 0], 34)  #dst_host_diff_srv_rate 
ZscoreNormalization(x_mat[:, 0], 35)  #dst_host_same_src_port_rate
ZscoreNormalization(x_mat[:, 0], 36)  #dst_host_srv_diff_host_rate
ZscoreNormalization(x_mat[:, 0], 37)  #dst_host_serror_rate
ZscoreNormalization(x_mat[:, 0], 38)  #dst_host_srv_serror_rate
ZscoreNormalization(x_mat[:, 0], 39)  #dst_host_rerror_rate
ZscoreNormalization(x_mat[:, 0], 40)  #dst_host_srv_rerror_rate

#文件写入操作
csv_writer = csv.writer(data_file)
i = 0
while i<len(x_mat[:, 0]):
    csv_writer.writerow(x_mat[i, :])
    i = i + 1
data_file.close()
