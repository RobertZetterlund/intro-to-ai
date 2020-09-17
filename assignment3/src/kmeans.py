# Author: {Tobias Lindroth & Robert Zetterlund}
# Adopted from: Phil Roth <mr.phil.roth@gmail.com>
# License: BSD 3 clause

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from numpy.random import default_rng


# SELECT NR OF CLUSTERS
n_clusters = 3

# Setup constants
colors = ["red", "blue", "green", "orange",
          "purple", "cyan", "black", "pink", "yellow"]
PATH = '../res/data_all.csv'
PHI = "phi"
PSI = "psi"
df = pd.read_csv(PATH)

# Get data to scatterplot
X = df[[PHI, PSI]]
random_state = 170


fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

## Function for getting good color instead of monochrome
def getColors(p): return colors[p]
vColors = np.vectorize(getColors)


# create 4 plots where we omit 25% of datapoints to see if similar clusters arise
for i in range(4):
    np.random.seed(i)
    # select indexes to remove
    index_to_remove = np.random.choice(X.index, size=len(X.index) // 4, replace=False)
    sub_X = X.drop(index_to_remove)
    # predict on subset of X
    y_pred = KMeans(n_clusters=n_clusters,
                    random_state=random_state).fit_predict(sub_X)
    # plot
    sub_X.plot.scatter(x=PHI, y=PSI, ax=ax[i // 2, i % 2 ], c=vColors(y_pred))


y_pred = KMeans(n_clusters=n_clusters,
               random_state=random_state).fit_predict(X)

df.plot.scatter(x=PHI, y=PSI, c=vColors(y_pred))
plt.yticks(np.arange(-180, 181, 40))
plt.xticks(np.arange(-180, 181, 40))
plt.title("Kmeans using " + str(n_clusters) + " number of clusters")
plt.show()
