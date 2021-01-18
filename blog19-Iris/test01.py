#导入数据集iris  
from sklearn.datasets import load_iris

#载入数据集  
iris = load_iris()

#输出数据集  
print(iris.data)

#输出真实标签  
print(iris.target)
print(len(iris.target))

#150个样本 每个样本4个特征  
print(iris.data.shape)
