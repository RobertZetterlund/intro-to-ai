# Author: {Tobias Lindroth & Robert Zetterlund}
# Adopted from: Phil Roth <mr.phil.roth@gmail.com>
# License: BSD 3 clause

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from numpy.random import default_rng


# SELECT NR OF CLUSTERS
n_clusters = 4

# Setup constants
colors = ["red", "blue", "green", "orange",
          "purple", "cyan", "black", "pink", "yellow"]
PATH = '../../res/data_all.csv'
PHI = "phi"
PSI = "psi"
RESIDUE_NAME = 'GLY'
df = pd.read_csv(PATH)


if RESIDUE_NAME:
    df = df.loc[df['residue name'] == RESIDUE_NAME]

# Get data to scatterplot
df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)


X = df[[PHI, PSI]]
random_state = 170

# Function for getting good color instead of monochrome
def getColors(p): return colors[p%len(colors)]
vColors = np.vectorize(getColors)


#fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

# create 4 plots where we omit 25% of datapoints to see if similar clusters arise
#for i in range(4):
#    np.random.seed(i)
#    # select indexes to remove
#    index_to_remove = np.random.choice(
#        X.index, size=len(X.index) // 4, replace=False)
#    sub_X = X.drop(index_to_remove)
#    # predict on subset of X
#    kmeans = KMeans(n_clusters=n_clusters,
#                    random_state=random_state)
#    y_pred = kmeans.fit_predict(sub_X)
#    # plot
#    sub_X.plot.scatter(x=PHI, y=PSI, ax=ax[i // 2, i % 2], c=vColors(y_pred))


kmeans = KMeans(n_clusters=n_clusters,
                random_state=random_state)

y_pred = kmeans.fit_predict(X)

df.plot.scatter(x=PHI, y=PSI, c=vColors(y_pred))

centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='k', zorder=10)

#plt.hlines(-110, -180,180)
#plt.vlines(0, -180,180)



plt.title("Kmeans using " + str(n_clusters) + " number of clusters")
plt.show()
