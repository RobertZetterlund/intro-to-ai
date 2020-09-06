import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Which countries have high life expectancy but have low GDP?
# For the sake of the assignment,
# lets assume that high and low represents is based on the standard deviation.
# To which extent can be set by adjusting the variable STD_CONSTANT below

# 0.253 is a z score indicating 60 (or 40) %.
STD_CONSTANT = 0
SELECTED_YEAR = 2016

# Setup constants
GDP = "Output-side real GDP per capita (2011 international-$)"
HOUSEHOLD = "Share of one person households (%)"
INTERNET = "Individuals using the Internet (% of population)"

# use pandas to read csv
df_gdp = pd.read_csv("../res/gdp.csv")
df_internet = pd.read_csv("../res/share-of-individuals-using-the-internet.csv")
df_households = pd.read_csv("../res/one-person-households.csv")

# filter data on selected year
gdp_entries = df_gdp[(df_gdp["Year"] == SELECTED_YEAR)]
internet_entries = df_internet[(df_internet["Year"] == SELECTED_YEAR)]
household_entries = df_households[(df_households["Year"] == SELECTED_YEAR)]


# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(gdp_entries, internet_entries, on=["Code", "Year", "Entity"])
merged_entries = pd.merge(merged_entries, household_entries, on=["Code", "Year", "Entity"])

print(merged_entries.count)

# get standard deviation and mean from entries
gdp_std = np.std(merged_entries[GDP])
gdp_mean = np.mean(gdp_entries[GDP])



highGdp = merged_entries[(merged_entries[GDP] >= gdp_mean + gdp_std * STD_CONSTANT )]

rest = merged_entries.drop(highGdp.index)


fig, ax = plt.subplots()


inputs = [(highGdp, "blue", "GDP per capita above the mean"),
            (rest, "gray", "GDP per capita below or equal to the mean")
          ]

for df, color, label in inputs:
    ax.scatter(df[HOUSEHOLD], df[INTERNET], c=color, s=75, label=label,
               alpha=0.8, edgecolors='none')   

ax.legend()

plt.xlabel(HOUSEHOLD)
plt.ylabel(INTERNET)
plt.savefig("../fig/intenet_household_gdp_2016.png")
plt.show()



