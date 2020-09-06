import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Setup constants
SELECTED_YEAR = 2010
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

# setup scatterplot
fig, ax = plt.subplots()
# scatterplot gdp as x, life-expectancy as y
plt.scatter(merged_entries[GDP], merged_entries[LIFE])
plt.xlabel("GDP per capita (2011 international-$)")
plt.ylabel("Life Expectancy (years)")
plt.savefig("../fig/gdp_life.png")
# plt.show()