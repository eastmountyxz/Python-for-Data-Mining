import pandas
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
 
from pandas.plotting import radviz
radviz(dataset, 'class')
 
from pandas.plotting import andrews_curves
andrews_curves(dataset, 'class')
 
from pandas.plotting import parallel_coordinates
parallel_coordinates(dataset, 'class')
plt.show()
