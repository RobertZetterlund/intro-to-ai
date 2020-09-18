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

neigh = NearestNeighbors(n_neighbors=200)
nbrs = neigh.fit(X)

# Get distances to the closest n_neighbors neighbors for each node
distances, indices = nbrs.kneighbors(X)

# Sort each node's distances to its closest n_neighbors neighbors
distances = np.sort(distances, axis=0)

# For each node, pick out the distance to the neighbor (out of closest n_neighbors) that is furthest away. 
distances = distances[:,1]

#Plot these distances
plt.plot(distances)

plt.show()