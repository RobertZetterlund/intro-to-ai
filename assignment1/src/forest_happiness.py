import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Setup constants
SELECTED_YEAR = 2010
HEADER_X = (
    "15.1.1 - Forest area as a proportion of total land area (%) - AG_LND_FRST (%)"
)
HEADER_Y = "World Happiness Report 2016 (Cantril Ladder (0=worst; 10=best))"

# use pandas to read csv
df_forest = pd.read_csv("../res/forest-area-as-share-of-land-area.csv")
df_happiness = pd.read_csv("../res/happiness-cantril-ladder.csv")

# filter data on selected year
forest_entries = df_forest[(df_forest["Year"] == SELECTED_YEAR)]
life_entries = df_happiness[(df_happiness["Year"] == SELECTED_YEAR)]

# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(forest_entries, life_entries, on=["Code", "Year", "Entity"])


# setup scatterplot
fig, ax = plt.subplots()
# scatterplot gdp as x, life-expectancy as y
plt.scatter(merged_entries[HEADER_X], merged_entries[HEADER_Y])
plt.xlabel("Forest area as share of land area")
plt.ylabel("Happiness")
plt.savefig('../fig/forest_happiness.png')
#plt.show()