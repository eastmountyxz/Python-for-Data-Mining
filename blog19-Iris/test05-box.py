import pandas
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

#读取csv数据
dataset = pandas.read_csv(url, names=names)
print(dataset.describe())

dataset.plot(kind='kde')
dataset.plot(kind='box', subplots=True, layout=(2,2), 
             sharex=False, sharey=False)
plt.show()
