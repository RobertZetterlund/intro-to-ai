# Author: {Tobias Lindroth & Robert Zetterlund}
# Adopted from: Phil Roth <mr.phil.roth@gmail.com>
# License: BSD 3 clause

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Setup constants
colors = ["red","blue","green","orange","purple","cyan","black", "pink", "yellow"]
PATH = '../res/data_all.csv'
PHI = "phi"
PSI = "psi"
df = pd.read_csv(PATH)

# Get data to scatterplot
X = df[[PHI, PSI]]
random_state = 170

y_pred = KMeans(n_clusters=4, random_state=random_state).fit_predict(X)

getColors = lambda p: colors[p]
vColors = np.vectorize(getColors)

df.plot.scatter(x=PHI, y=PSI, c=vColors(y_pred))
plt.yticks(np.arange(-180, 181, 40))
plt.xticks(np.arange(-180, 181, 40))
plt.show()