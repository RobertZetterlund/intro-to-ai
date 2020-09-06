## Author: {Tobias Lindroth & Robert Zetterlund}
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Which countries have high life expectancy but have low GDP?
# For the sake of the assignment,
# lets assume that high and low represents is based on the standard deviation.
# To which extent can be set by adjusting the variable STD_CONSTANT below

# 0.253 is a z score indicating 60 (or 40) %.
STD_CONSTANT = 0.253
SELECTED_YEAR = 2017

# Allow for argument in unix. eg. 'python task_b.py 0.2 1999'
if len(sys.argv) >= 2:
    STD_CONSTANT = float(sys.argv[1])
    if len(sys.argv) >= 3:
        SELECTED_YEAR = float(sys.argv[2])

# Setup constants
GDP = "Output-side real GDP per capita (2011 international-$)"
LIFE = "Life expectancy (years)"

# use pandas to read csv
df_gdp = pd.read_csv("../res/gdp.csv")
df_life = pd.read_csv("../res/life-expectancy.csv")

# filter data on selected year
gdp_entries = df_gdp[(df_gdp["Year"] == SELECTED_YEAR)]
life_entries = df_life[(df_life["Year"] == SELECTED_YEAR)]

# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(gdp_entries, life_entries, on=["Code", "Year", "Entity"])

# get standard deviation and mean from entries
gdp_std = np.std(merged_entries[GDP])
gdp_mean = np.mean(merged_entries[GDP])

life_std = np.std(merged_entries[LIFE])
life_mean = np.mean(merged_entries[LIFE])

highLife = merged_entries[(merged_entries[LIFE] > life_mean + life_std * STD_CONSTANT )]
highLifeLowGdp =  highLife[(highLife[GDP] < gdp_mean - gdp_std * STD_CONSTANT)]
rest = merged_entries.drop(highLifeLowGdp.index)


fig, ax = plt.subplots()


inputs = [(highLifeLowGdp, "blue", "High life expectancy, low GDP"),
            (rest, "gray", "Other")
          ]

for df, color, label in inputs:
    ax.scatter(df[GDP], df[LIFE], c=color, s=75, label=label,
               alpha=0.8, edgecolors='none')
    
ax.legend()

plt.xlabel("GDP per capita ($)")
plt.ylabel("Life expectancy (years)")
plt.savefig("../fig/gdp_life_b.png")
plt.show()


print(len(highLifeLowGdp))
print(len(rest))
# print countries having a high life expectancy and a low gdp
if len(highLifeLowGdp) > 0:
    print("These countries have high life expectancy and a low gdp: \n")
    print(highLifeLowGdp["Entity"].to_frame().to_string(index=False))
else:
    print("There are no countries with a high life expectancy and a low gdp")
