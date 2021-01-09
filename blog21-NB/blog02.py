import numpy as np  
from sklearn.naive_bayes import GaussianNB  
X = np.array([[-1,-1], [-2,-2], [-3,-3], [-4,-4], [-5,-5], 
              [1,1], [2,2], [3,3]])  
y = np.array([1, 1, 1, 1, 1, 2, 2, 2])  
clf = GaussianNB()  
clf.partial_fit(X,y,classes=[1,2],
                sample_weight=np.array([0.05,0.05,0.1,0.1,0.1,0.2,0.2,0.2]))  
print(clf.class_prior_)
print(clf.predict([[-6,-6],[4,5],[2,5]]))
print(clf.predict_proba([[-6,-6],[4,5],[2,5]]))
