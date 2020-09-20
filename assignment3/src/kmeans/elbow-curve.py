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
RESIDUE_NAME = "PRO"
df = pd.read_csv(PATH)

if RESIDUE_NAME:
    df = df.loc[df['residue name'] == RESIDUE_NAME]

df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)

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
plt.title('Elbow curve for ' + str(RESIDUE_NAME))
plt.show()