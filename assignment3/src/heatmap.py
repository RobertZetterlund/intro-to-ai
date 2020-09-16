# Author: {Tobias Lindroth & Robert Zetterlund}
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme()


# SELECT AMOUNT OF BOXES FOR HEATMAP
nr_boxes = 18

# Setup constants
PATH = '../res/data_all.csv'
PHI = "phi"
PSI = "psi"
boxsize = 360 // nr_boxes
ticks = np.arange(-180, 180, boxsize)

# use pandas to read csv
df = pd.read_csv(PATH)
df = df[[PHI, PSI]]
df = df.astype(int)

# apply function which gets index based on value
df = df.apply(lambda x: x // boxsize + (nr_boxes // 2))

# create matrix for heatmap, init as zeros
matrix = np.zeros((nr_boxes, nr_boxes), dtype=int)

# increment values in matrix based on index
for row in df.itertuples(index=False):
    matrix[row[0]][row[1]] += 1

# check if all datapoints have been counted'
print("Have all " + str(len(df.index)) + " entries been counted? True/False")
print(len(df.index) == np.sum(matrix))

# create heatmap
ax = sns.heatmap(matrix, xticklabels=ticks, yticklabels=ticks)

plt.show()
