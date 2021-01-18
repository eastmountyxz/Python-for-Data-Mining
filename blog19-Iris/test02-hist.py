import pandas
import matplotlib.pyplot as plt

#导入数据集iris  
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

#读取csv数据
dataset = pandas.read_csv(url, names=names)
print(dataset.describe())

#直方图 histograms
dataset.hist()
plt.show()

