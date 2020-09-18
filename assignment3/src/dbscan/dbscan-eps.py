import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

PATH = '../../res/data_all.csv'
PHI = "phi"
PSI = "psi"
df = pd.read_csv(PATH)

df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)

X = df[[PHI, PSI]]

neigh = NearestNeighbors(n_neighbors=50)
nbrs = neigh.fit(X)
distances, indices = nbrs.kneighbors(X)

distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)

plt.show()