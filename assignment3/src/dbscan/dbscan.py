# Author: {Tobias Lindroth & Robert Zetterlund}
# Adopted from: https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt

# good for 200: eps 35, min_samples=3
# good for 500: eps 30, min_samples=9
# good for all: eps 19, min_samples=42

# #############################################################################
# Get data

PATH = '../../res/data_200.csv'
PHI = "phi"
PSI = "psi"
df = pd.read_csv(PATH)

df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)

X = df[[PHI, PSI]]

# #############################################################################
# Compute DBSCAN
db = DBSCAN(eps=35, min_samples=3).fit(X)

# create array same size as dataset, init as all false
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
# Take array and make boolean true for indices of core nodes
core_samples_mask[db.core_sample_indices_] = True

labels = db.labels_

# #############################################################################
# Plot result

# Take array of labels and turn into set.
unique_labels = set(labels)

cmap = plt.get_cmap("RdYlGn")


# Using the cmap gradient, ensure picked colors are as far away from eachother
# using linspace from 0,1
colors = [cmap(each)
          for each in np.linspace(0, 1, len(unique_labels))]


# For all labels, zip with corresponding color and iterate.
for u_label, color in zip(unique_labels, colors):
    # u_label is -1 if not part of cluster, ie. noise
    isNoise = u_label == -1

    # make unassigned datapoints grey
    if isNoise:
        color = [232/255, 236/255, 241/255, 0.8]

    # create mask for labels, used for selecting which datapoints to plot
    class_member_mask = (labels == u_label)
    
    # PLOT NON-CORE DATAPOINTS
    # Filter xy, get only non-core datapoints 
    non_core = X[class_member_mask & ~core_samples_mask]
    plt.plot(non_core[PHI], non_core[PSI], 'o', markerfacecolor=tuple(color),
             markeredgecolor="black", markersize=6)

    # PLOT CORE DATAPOINTS
    # Filter X, get only core datapoints
    core = X[class_member_mask & core_samples_mask]
    plt.plot(core[PHI], core[PSI], 'o', markerfacecolor=tuple(color),
             markeredgecolor='black', markersize=14)


# Number of clusters in labels. if we have noise (-1), n_clusters should exclude that
n_clusters_ = len(set(labels)) - 1 if (-1 in labels) else 0
n_noise_ = list(labels).count(-1)

#print('Estimated number of clusters: %d' % n_clusters_)
#print('Estimated number of noise points: %d' % n_noise_)
# print("Silhouette Coefficient: %0.3f"
#      % metrics.silhouette_score(X, labels))

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
