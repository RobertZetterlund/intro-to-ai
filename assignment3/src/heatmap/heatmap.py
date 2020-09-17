# Author: {Tobias Lindroth & Robert Zetterlund}
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme()


# SELECT AMOUNT OF BOXES FOR HEATMAP
nr_boxes = 18

# Setup constants
PATH = '../../res/data_all.csv'
PHI = "phi"
PSI = "psi"
BOX_SIZE = 360 // nr_boxes
INDEX_OFFSET = nr_boxes // 2
Y_TICKS = np.arange(-180, 180, BOX_SIZE)
X_TICKS = np.arange(-180,180, BOX_SIZE)
# use pandas to read csv
df = pd.read_csv(PATH)
df = df[[PHI, PSI]]
df = df.astype(int)

# apply function which gets index based on value
df = df.apply(lambda row: row // BOX_SIZE + INDEX_OFFSET )

# create matrix for heatmap, init as zeros
matrix = np.zeros((nr_boxes, nr_boxes), dtype=int)

# increment values in matrix based on index
for row in df.itertuples(index=False):
    matrix[row[1]][row[0]] += 1

# check if all datapoints have been counted'
print("Have all " + str(len(df.index)) + " entries been counted? True/False")
print(len(df.index) == np.sum(matrix))

# in order to get similar axis distr as scatterplot, flip matrix in y, also flip yticks
matrix = np.flip(matrix, axis=0)
Y_TICKS = np.flip(Y_TICKS)

# create heatmap
ax = sns.heatmap(matrix, xticklabels=X_TICKS, yticklabels=Y_TICKS)
plt.xlabel("phi")
plt.ylabel("psi")

plt.show()
