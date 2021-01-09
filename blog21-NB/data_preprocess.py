import os
import csv

fw1 = open('seed_x.csv', 'w', newline='')
fw2 = open('seed_y.csv', 'w', newline='')
writer1 = csv.writer(fw1)
writer2 = csv.writer(fw2)

with open('seed.txt','r',encoding='utf-8') as f:
    for data in f.readlines():
        #print(data)
        value = data.split(" ")
        x0 = value[0]
        x1 = value[1]
        x2 = value[2]
        x3 = value[3]
        x4 = value[4]
        x5 = value[5]
        x6 = value[6]
        y = value[7]
        
        #文件写入
        writer1.writerow([x0,x1,x2,x3,x4,x5,x6])
        writer2.writerow(y)

fw1.close()
fw2.close()
