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
df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)
sns.kdeplot(x=df[PHI], y=df[PSI], fill=True, cmap="rocket", cbar=True, thresh=0, levels=50)
plt.show()