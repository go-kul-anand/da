from sklearn.datasets import load_diabetes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
print("Shape of X",X.shape)
print("Shape of y",y.shape)
knn.fit(X, y)
knn.predict([[10,15,20,30,13,12,6,8,7,22]])
X_new = [[5,1,6,8,7,3,2,1,10,15],[15,13,5,9,7,3,6,4,1,1]]
knn.predict(X_new)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
knn.predict(X_new)
logreg = LogisticRegression(solver='liblinear')
logreg.fit(X, y)
logreg.predict(X_new)
