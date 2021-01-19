from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

iris = load_iris()
#训练集
train_data = np.concatenate((iris.data[0:40, :], iris.data[50:90, :], iris.data[100:140, :]), axis = 0)
train_target = np.concatenate((iris.target[0:40], iris.target[50:90], iris.target[100:140]), axis = 0)
#测试集
test_data = np.concatenate((iris.data[40:50, :], iris.data[90:100, :], iris.data[140:150, :]), axis = 0)
test_target = np.concatenate((iris.target[40:50], iris.target[90:100], iris.target[140:150]), axis = 0)

#训练
clf = DecisionTreeClassifier()
clf.fit(train_data, train_target)
predict_target = clf.predict(test_data)
print(predict_target)

#预测结果与真实结果比对
print(sum(predict_target == test_target))

#输出准确率 召回率 F值
from sklearn import metrics
print(metrics.classification_report(test_target,predict_target))
print(metrics.confusion_matrix(test_target,predict_target))
X = test_data
L1 = [n[0] for n in X]
print(L1)
L2 = [n[1] for n in X]
print(L2)

import matplotlib.pyplot as plt
plt.scatter(L1, L2, c=predict_target, marker='x')  #cmap=plt.cm.Paired
plt.title("DecisionTreeClassifier")  
plt.show()
