# Author: {Tobias Lindroth & Robert Zetterlund}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
import numpy as np


# Setup constants
PATH = '../res/data_all.csv'
PHI = "phi"
PSI = "psi"



# use pandas to read csv
df = pd.read_csv(PATH)
sns.kdeplot(x=df[PHI], y=df[PSI], fill=True, cmap="rocket")
plt.yticks(np.arange(-180, 181, 40))
plt.xticks(np.arange(-180, 181, 40))
plt.show()