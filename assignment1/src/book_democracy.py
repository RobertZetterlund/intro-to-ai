import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Setup constants
SELECTED_YEAR = 1990
HEADER_X = "Unique booktitles per million inhabitants"
HEADER_Y = "Political Regime"

# use pandas to read csv
df_books = pd.read_csv("../res/books.csv")
df_democracy = pd.read_csv("../res/democracy-level.csv")

# filter data on selected year
df_books = df_books[(df_books["Year"] == SELECTED_YEAR)]
df_democracy = df_democracy[(df_democracy["Year"] == SELECTED_YEAR)]


# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(df_democracy, df_books, on=["Entity"])
merged_entries = merged_entries[merged_entries["Political Regime"] != -20]


# setup scatterplot
fig, ax = plt.subplots()
# scatterplot gdp as x, life-expectancy as y
plt.scatter(merged_entries[HEADER_X], merged_entries[HEADER_Y])
plt.xlabel(HEADER_X)
plt.ylabel(HEADER_Y)
plt.show()
