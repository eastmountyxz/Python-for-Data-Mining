import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='SimHei', size=13)
 
num = np.array([13325, 9403, 9227, 8651])
ratio = np.array([0.75, 0.76, 0.72, 0.75])
men = num * ratio
women = num * (1-ratio)
x = [u'聊天',u'支付',u'团购\n优惠券',u'在线视频']
 
width = 0.5
idx = np.arange(len(x))
plt.bar(idx, men, width, color='red', label=u'男性用户')
plt.bar(idx, women, width, bottom=men, color='yellow', label=u'女性用户')
plt.xlabel(u'应用类别')
plt.ylabel(u'男女分布')
plt.xticks(idx+width/2, x, rotation=40)
plt.legend()
plt.show()
