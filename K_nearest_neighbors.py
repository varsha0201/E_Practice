from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
iris = load_iris()

X= iris.data
y= iris.target

X.shape
y.shape

knn = KNeighborsClassifier(n_neighbors=4)
knn

knn.fit(X,y)
a = np.array([4,5,6,2])
a.shape

knn.predict([a])

