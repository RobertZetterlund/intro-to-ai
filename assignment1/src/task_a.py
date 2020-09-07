## Author: {Tobias Lindroth & Robert Zetterlund}
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Which countries have a life expectancy higher
# than one standard deviation above the mean?

SELECTED_YEAR = 2017
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
life_std = np.std(merged_entries[LIFE])
life_mean = np.mean(merged_entries[LIFE])

high_life = merged_entries[merged_entries[LIFE] > life_mean + life_std]

rest = merged_entries.drop(high_life.index)

fig, ax = plt.subplots()

inputs = [
    (high_life, "blue", "Life Expectancy one standard deviation above mean"),
    (rest, "gray", "Other"),
]

for df, color, label in inputs:
    ax.scatter(
        df[GDP], df[LIFE], c=color, s=75, label=label, alpha=0.8, edgecolors="none"
    )

ax.legend()

print(high_life["Entity"].to_frame().to_string(index=False))

plt.xlabel("GDP per capita")
plt.ylabel("Life Expectancy")
# plt.savefig("../fig/gdp_life_b.png")
plt.show()