import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Setup constants
SELECTED_YEAR = 2010
HEADER_TITLE_X = (
    "Average annual hours worked by persons engaged (hours per person engaged)"
)
HEADER_TITLE_Y = "World Happiness Report 2016 (Cantril Ladder (0=worst; 10=best))"

# use pandas to read csv
df_forest = pd.read_csv("../res/annual-working-hours-per-persons-engaged.csv")
df_happiness = pd.read_csv("../res/happiness-cantril-ladder.csv")

# filter data on selected year
forest_entries = df_forest[(df_forest["Year"] == SELECTED_YEAR)]
life_entries = df_happiness[(df_happiness["Year"] == SELECTED_YEAR)]

# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(forest_entries, life_entries, on=["Code", "Year", "Entity"])


# setup scatterplot
fig, ax = plt.subplots()
# scatterplot gdp as x, life-expectancy as y
plt.scatter(merged_entries[HEADER_TITLE_X], merged_entries[HEADER_TITLE_Y])
plt.xlabel("Forest area as share of land area")
plt.ylabel("Happiness")
plt.show()