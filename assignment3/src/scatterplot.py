# Author: {Tobias Lindroth & Robert Zetterlund}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()

# Setup constants
PATH = '../res/data_200.csv'
PHI = "phi"
PSI = "psi"

# use pandas to read csv
df = pd.read_csv(PATH)
df.plot.scatter(x=PHI, y=PSI)
plt.show()