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
PATH = '../../res/data_all.csv'
PHI = "phi"
PSI = "psi"
df = pd.read_csv(PATH)

# Get data to scatterplot
X = df[[PHI, PSI]]

# shift phi and psi by certain amount.
# shift phi by 180, new range is 0>->360
# shift psi by 70, new range is -110>->250
df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)

X = df[[PHI, PSI]]

random_state = 170


# Function for getting good color instead of monochrome
def getColors(p): return colors[p]


vColors = np.vectorize(getColors)


y_pred = KMeans(n_clusters=n_clusters,
                random_state=random_state).fit_predict(X)

df.plot.scatter(x=PHI, y=PSI, c=vColors(y_pred))
plt.xticks(np.arange(0, 361, 40))
plt.yticks(np.arange(-110, 251, 40))
plt.title("Kmeans using " + str(n_clusters) + " number of clusters, with shifted axises")
plt.show()
