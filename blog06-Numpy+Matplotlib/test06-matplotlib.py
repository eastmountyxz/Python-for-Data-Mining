import matplotlib.pyplot as plt
 
mm = [45, 30, 25]             #每一块占得比例，总和为100
n = mm[0]+mm[1]+mm[2]
a = (mm[0]*1.0*100/n)
b = (mm[1]*1.0*100/n)
c = (mm[2]*1.0*100/n)
print(a, b, c, n)
fracs = [a, b, c]
 
explode=(0, 0, 0.08)             #离开整体的距离，看效果
labels = 'A', 'B', 'C'           #对应每一块的标志
 
plt.pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90, colors = ("g", "r", "y"))
                                 # startangle是开始的角度，默认为0，从这里开始按逆时针方向依次展开
 
plt.title('Raining Hogs and Dogs')   #标题
 
plt.show()
