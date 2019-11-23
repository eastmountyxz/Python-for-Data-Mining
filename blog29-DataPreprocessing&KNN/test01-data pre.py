#coding:utf-8
import numpy as np
import pandas as pd
import csv

"""
功能：数据预处理 将KDD99数据集中字符型转换为数值型
原文：https://blog.csdn.net/asialee_bird/article/details/80491256

强烈推荐博友们阅读asialee_bird大神的文章及Github代码，非常厉害的一位博主。
修订：Eastmount 2019-11-22
"""

#label_list为全局变量
global label_list  

#文件名
source_file='kddcup.data_10_percent_corrected'
handled_file='kddcup.data_10_percent_corrected.csv'

#文件写入操作 wb+删除多余空行
data_file = open(handled_file,'wb+')


#将相应的非数字类型转换为数字标识即符号型数据转化为数值型数据
def find_index(x,y):
    return [i for i in range(len(y)) if y[i]==x]


#定义将源文件行中3种协议类型转换成数字标识的函数
def handleProtocol(inputs):
    protocol_list=['tcp','udp','icmp']
    if inputs[1] in protocol_list:
        return find_index(inputs[1], protocol_list)[0]


#定义将源文件行中70种网络服务类型转换成数字标识的函数
def handleService(inputs):
   service_list=['aol','auth','bgp','courier','csnet_ns','ctf','daytime','discard','domain','domain_u',
                 'echo','eco_i','ecr_i','efs','exec','finger','ftp','ftp_data','gopher','harvest','hostnames',
                 'http','http_2784','http_443','http_8001','imap4','IRC','iso_tsap','klogin','kshell','ldap',
                 'link','login','mtp','name','netbios_dgm','netbios_ns','netbios_ssn','netstat','nnsp','nntp',
                 'ntp_u','other','pm_dump','pop_2','pop_3','printer','private','red_i','remote_job','rje','shell',
                 'smtp','sql_net','ssh','sunrpc','supdup','systat','telnet','tftp_u','tim_i','time','urh_i','urp_i',
                 'uucp','uucp_path','vmnet','whois','X11','Z39_50']
   if inputs[2] in service_list:
       return find_index(inputs[2],service_list)[0]


#定义将源文件行中11种网络连接状态转换成数字标识的函数
def handleFlag(inputs):
    flag_list=['OTH','REJ','RSTO','RSTOS0','RSTR','S0','S1','S2','S3','SF','SH']
    if inputs[3] in flag_list:
        return find_index(inputs[3],flag_list)[0]


#定义将源文件行中攻击类型转换成数字标识的函数(训练集中共出现了22个攻击类型，而剩下的17种只在测试集中出现)
def handleLabel(inputs):
    label_list=['normal.', 'buffer_overflow.', 'loadmodule.', 'perl.', 'neptune.', 'smurf.',
                'guess_passwd.', 'pod.', 'teardrop.', 'portsweep.', 'ipsweep.', 'land.', 'ftp_write.',
                'back.', 'imap.', 'satan.', 'phf.', 'nmap.', 'multihop.', 'warezmaster.', 'warezclient.',
                'spy.', 'rootkit.']
    #在函数内部使用全局变量并修改它
    global label_list  
    if inputs[41] in label_list:
        return find_index(inputs[41],label_list)[0]
    else:
        label_list.append(inputs[41])
        return find_index(inputs[41],label_list)[0]


#主函数
if __name__=='__main__':
    #循环读取文件数据
    with open(source_file,'r') as data_source:
        csv_reader = csv.reader(data_source)
        csv_writer = csv.writer(data_file)
        count = 0   #行数
        for row in csv_reader:
            temp_line=np.array(row)                     
            temp_line[1] = handleProtocol(row)       #将源文件行中3种协议类型转换成数字标识
            temp_line[2] = handleService(row)        #将源文件行中70种网络服务类型转换成数字标识
            temp_line[3] = handleFlag(row)             #将源文件行中11种网络连接状态转换成数字标识
            temp_line[41] = handleLabel(row)         #将源文件行中23种攻击类型转换成数字标识
            csv_writer.writerow(temp_line)
            count += 1
            
            #输出每行数据中所修改后的状态
            #print(count,'status:',temp_line[1],temp_line[2],temp_line[3],temp_line[41])
        data_file.close()

