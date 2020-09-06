## Author: {Tobias Lindroth & Robert Zetterlund}

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Setup constants
SELECTED_YEAR = 2010
HEADER_X = "UN Population Division (Median Age) (2017) (years)"
HEADER_Y = "World Happiness Report 2016 (Cantril Ladder (0=worst; 10=best))"

# use pandas to read csv
df_x = pd.read_csv("../res/median-age.csv")
dy_y = pd.read_csv("../res/happiness-cantril-ladder.csv")

# filter data on selected year
x_entries = df_x[(df_x["Year"] == SELECTED_YEAR)]
y_entries = dy_y[(dy_y["Year"] == SELECTED_YEAR)]

# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(x_entries, y_entries, on=["Code", "Year", "Entity"])


# setup scatterplot
fig, ax = plt.subplots()
# scatterplot gdp as x, life-expectancy as y
plt.scatter(merged_entries[HEADER_X], merged_entries[HEADER_Y])
plt.xlabel(HEADER_X)
plt.ylabel(HEADER_Y)
plt.savefig("../fig/median-age_happiness.png")
