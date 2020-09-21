# Author: {Tobias Lindroth & Robert Zetterlund}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
import numpy as np


# Setup constants
PATH = '../res/data_all.csv'
PHI = "phi"
PSI = "psi"

RESIDUE_NAME = "PRO"
df = pd.read_csv(PATH)

df[PHI] = df[PHI].apply(lambda phi: phi + 360 if phi < 0 else phi)
df[PSI] = df[PSI].apply(lambda psi: psi + 360 if psi < -100 else psi)


df_residue = df.loc[df['residue name'] == RESIDUE_NAME]
df_rest = df.loc[df['residue name'] != RESIDUE_NAME]

ax = df_rest.plot.scatter(x=PHI, y=PSI, c="grey", alpha=0.2, label="dataset")
df_residue.plot.scatter(x=PHI, y=PSI, c="green", ax=ax, alpha=0.5, label=RESIDUE_NAME )

plt.show()