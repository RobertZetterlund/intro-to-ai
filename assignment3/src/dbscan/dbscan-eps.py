import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

PATH = '../../res/data_all.csv'
PHI = "phi"
PSI = "psi"
RESIDUE_NAME = ""
df = pd.read_csv(PATH)


if RESIDUE_NAME:
    df = df.loc[df['residue name'] == RESIDUE_NAME]

df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)

X = df[[PHI, PSI]]

neigh = NearestNeighbors(n_neighbors=200)
nbrs = neigh.fit(X)

# Get distances to the closest n_neighbors neighbors for each node
(distances,_) = nbrs.kneighbors(X)

# Sort each node's distances to its closest n_neighbors neighbors
distances = np.sort(distances, axis=0)


# For each node, pick out the distance to the neighbor (out of closest n_neighbors) that is furthest away.
distances = distances[:, -1]

# find index of largest difference (make a distinction of 28500,
# since the plot looks exponental and we're only interested in "elbow" area.)
index = np.diff(distances[0:27000]).argmax()

print("The largest difference is at x=" + str(index) + ", y=" + str(distances[index]))
# Plot these distances
plt.plot(distances)
plt.hlines(distances[index], 0, 30000, colors = ["red"])

plt.show()
