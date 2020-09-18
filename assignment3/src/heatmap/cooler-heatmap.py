# Author: {Tobias Lindroth & Robert Zetterlund}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
import numpy as np


# Setup constants
PATH = '../../res/data_all.csv'
PHI = "phi"
PSI = "psi"



# use pandas to read csv
df = pd.read_csv(PATH)

# Translate values
df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)

#Plot heatmap
sns.kdeplot(data=df[PHI], data2=df[PSI], fill=True, cmap="rocket")
plt.yticks(np.arange(-100, 260, 40))
plt.xticks(np.arange(0, 360, 40))
plt.show()