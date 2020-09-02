import numpy as np
import pandas as pd

SELECTED_YEAR = 2010
HEADER_TITLE = "Life expectancy (years)"

df = pd.read_csv("life-expectancy.csv")

# Extract data entries from dataframe where year is SELECTED YEAR, essentially filter
entries_from_year = df[(df["Year"] == SELECTED_YEAR)]

# Calculate standard deviation and mean
life_std = np.std(entries_from_year[HEADER_TITLE])
life_mean = np.mean(entries_from_year[HEADER_TITLE])

# get countries one std above average
top_countries = entries_from_year[
    entries_from_year[HEADER_TITLE] > life_mean + life_std
]

# print countries being one std above the mean
print(top_countries["Entity"])
