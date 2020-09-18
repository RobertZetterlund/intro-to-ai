# Author: {Tobias Lindroth & Robert Zetterlund}
# Adopted from: Phil Roth <mr.phil.roth@gmail.com>
# License: BSD 3 clause

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Setup constants
colors = ["red","blue","green","orange","purple","cyan","black", "pink", "yellow"]
PATH = '../../res/data_all.csv'
PHI = "phi"
PSI = "psi"
RESIDUE_NAME = ""
df = pd.read_csv(PATH)




if RESIDUE_NAME:
    df = df.loc[df['residue name'] == RESIDUE_NAME]

# Get data to scatterplot
X = df[[PHI, PSI]]
random_state = 170

distorsions = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    #inertia is sum of squared distances of samples to their closest cluster center.
    distorsions.append(kmeans.inertia_)

fig = plt.figure()
plt.plot(range(2, 10), distorsions)
plt.grid(True)
plt.title('Elbow curve')
plt.show()