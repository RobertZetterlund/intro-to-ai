import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt


# For the sake of the assignment,
# lets assume that high and low represents is based on the standard deviation.
# To which extent can be set by adjusting the variable STD_CONSTANT below


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

# filter based on having strong economy
strong_economy = merged_entries[
    merged_entries[GDP] > gdp_mean + gdp_std * STD_CONSTANT
]

weak_economy =  merged_entries[
    merged_entries[GDP] <= gdp_mean + gdp_std * STD_CONSTANT
]
# filter based on having not high life expectancy
not_high_life_strong_economy = strong_economy[
    strong_economy[LIFE] < life_mean + life_std * STD_CONSTANT
]

high_life_strong_economy = strong_economy[
    strong_economy[LIFE] > life_mean + life_std * STD_CONSTANT
]



inputs = [(not_high_life_strong_economy, "blue", "Strong economy, not a high life expectancy"), 
          (high_life_strong_economy, "green", "Strong economy, high life expectancy"),
          (weak_economy, "gray", "Not a strong economy") ]
fig, ax = plt.subplots()

for df, color, label in inputs:
    ax.scatter(df[GDP], df[LIFE], c=color, s=75, label=label,
               alpha=0.8, edgecolors='none')

ax.legend()    

plt.xlabel("GDP per capita ($)")
plt.ylabel("Life expectancy (years)")
plt.savefig("../fig/gdp_life_c.png")

plt.show()               

# print countries having a high life expectancy and a low gdp
if len(not_high_life_strong_economy['Entity']) > 0:
    print("These countries have strong economy but not a high life expectancy: \n")
    print(not_high_life_strong_economy['Entity'])
else:
    print("There are no countries with a low life expectancy and a strong economy")
