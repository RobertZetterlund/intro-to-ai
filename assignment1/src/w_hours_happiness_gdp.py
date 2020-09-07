## Author: {Tobias Lindroth & Robert Zetterlund}

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

SELECTED_YEAR = 2010

# Setup constants
GDP = "Output-side real GDP per capita (2011 international-$)"
HAPPINESS = "World Happiness Report 2016 (Cantril Ladder (0=worst; 10=best))"
W_HOURS = "Average annual hours worked by persons engaged (hours per person engaged)"

# use pandas to read csv
df_gdp = pd.read_csv("../res/gdp.csv")
df_whours = pd.read_csv("../res/annual-working-hours-per-persons-engaged.csv")
df_happy = pd.read_csv("../res/happiness-cantril-ladder.csv")

# filter data on selected year
gdp_entries = df_gdp[(df_gdp["Year"] == SELECTED_YEAR)]
whours_entries = df_whours[(df_whours["Year"] == SELECTED_YEAR)]
happy_entries = df_happy[(df_happy["Year"] == SELECTED_YEAR)]


# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(gdp_entries, whours_entries, on=["Code", "Year", "Entity"])
merged_entries = pd.merge(merged_entries, happy_entries, on=["Code", "Year", "Entity"])

print(merged_entries.count)

# get standard deviation and mean from entries
gdp_std = np.std(merged_entries[GDP])
gdp_mean = np.mean(gdp_entries[GDP])


highGdp = merged_entries[(merged_entries[GDP] > gdp_mean)]

rest = merged_entries.drop(highGdp.index)


fig, ax = plt.subplots()


inputs = [
    (highGdp, "blue", "GDP per capita above the mean"),
    (rest, "gray", "GDP per capita below or equal to the mean"),
]

for df, color, label in inputs:
    ax.scatter(
        df[W_HOURS],
        df[HAPPINESS],
        c=color,
        s=75,
        label=label,
        alpha=0.8,
        edgecolors="none",
    )

ax.legend()

plt.title("Working hours and happiness (2010)")

plt.xlabel(W_HOURS)
plt.ylabel(HAPPINESS)
plt.savefig("../fig/w-hours_happiness_gdp.png")
plt.show()
