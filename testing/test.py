import sys
import pandas
import numpy as np
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, sharex = 'all', sharey = 'all')
for i in range(4):
    df = pandas.read_csv(sys.argv[i+1], sep=' ')
    xValues = df['x']
    yValues = df['y']
    axs[ i // 2, i % 2 ].scatter(xValues, yValues)
    axs[ i // 2, i % 2 ].set_title(sys.argv[i+1])
# Hide x labels and tick labels for top plots
# and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.show()