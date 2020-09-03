import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# For the sake of the assignment,
# lets assume that high and low represents is based on the standard deviation.
# To which extent can be set by adjusting the variable STD_CONSTANT below

# 0.253 is a z score indicating 60 (or 40) %.
STD_CONSTANT = 0.253
SELECTED_YEAR = 2010

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

#    GDP MEAN
#  red   | orange
# -------|------- LIFE MEAN
# purple | blue

col = np.where(
    merged_entries[LIFE] > life_mean - life_std * STD_CONSTANT,
    np.where(merged_entries[GDP] < gdp_mean + gdp_std * STD_CONSTANT, "red", "orange"),
    np.where(merged_entries[GDP] < gdp_mean + gdp_std * STD_CONSTANT, "purple", "blue"),
)

fig, ax = plt.subplots()


scatter = ax.scatter(
    merged_entries[GDP],
    merged_entries[LIFE],
    c=col,
    s=75,
    alpha=0.8,
    edgecolors="none",
)


# plt.legend()
plt.xlabel("GDP")
plt.ylabel("Life Expectancy")
plt.savefig("../fig/gdp_life_b.png")
plt.show()

# filter based on having high life-expectancy
high_life = merged_entries[merged_entries[LIFE] > life_mean + life_std * STD_CONSTANT]
# filter based on having low gdp
high_life_low_gdp = high_life[high_life[GDP] < gdp_mean - gdp_std * STD_CONSTANT]

# print countries having a high life expectancy and a low gdp
if len(high_life_low_gdp) > 0:
    print("These countries have high life expectancy and a low gdp: \n")
    print(high_life_low_gdp["Entity"])
else:
    print("There are no countries with a high life expectancy and a low gdp")
