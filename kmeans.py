from sklearn.cluster import KMeans
import numpy as np

if __name__ == '__main__':
    km = KMeans(2, random_state=0)
    X = np.array([[1, 2], [1, 4], [1, 0],[10, 2], [10, 4], [10, 0]])
    km.fit(X)
    print(km.labels_)
    print(km.predict([[0, 0], [12, 3]]))


