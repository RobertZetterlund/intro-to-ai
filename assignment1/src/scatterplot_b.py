import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Setup constants
SELECTED_YEAR = 2010
HEADER_TITLE_GDP = "Output-side real GDP per capita (2011 international-$)"
HEADER_TITLE_LIFE = "Life expectancy (years)"

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

col = np.where(
    merged_entries[HEADER_TITLE_GDP] < 40000,
    "b",
    np.where(merged_entries[HEADER_TITLE_LIFE] > 50, "r", "y"),
)

plt.scatter(merged_entries[HEADER_TITLE_GDP], merged_entries[HEADER_TITLE_LIFE], c=col)
plt.xlabel("GDP")
plt.ylabel("Life Expectancy")
# plt.savefig('../fig/gdp_life_b.png')
plt.show()