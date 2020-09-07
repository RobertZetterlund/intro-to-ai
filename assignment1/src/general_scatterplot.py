## Author: {Tobias Lindroth & Robert Zetterlund}

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    description="Creates a scatterplot. Expects the csv files to have the columns Code, Year and Entity"
)
parser.add_argument("csv_x", type=str, help="CSV file 1")
parser.add_argument("csv_y", type=str, help="CSV file 2")
parser.add_argument(
    "column_x", type=str, help="Title of column in file 1 to put on x-axis"
)
parser.add_argument(
    "column_y", type=str, help="Title of column in file 2 to put on y-axis"
)
parser.add_argument("year", type=int, help="The year to compare on")

parser.add_argument("--output", type=str, help="name of output file")

args = parser.parse_args()

# Setup constants
SELECTED_YEAR = args.year
HEADER_TITLE_X = args.column_x
HEADER_TITLE_Y = args.column_y

# use pandas to read csv
df_x = pd.read_csv("../res/" + args.csv_x)
df_y = pd.read_csv("../res/" + args.csv_y)

# filter data on selected year
x_entries = df_x[(df_x["Year"] == SELECTED_YEAR)]
y_entries = df_y[(df_y["Year"] == SELECTED_YEAR)]

# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(x_entries, y_entries, on=["Code", "Year", "Entity"])


# setup scatterplot
fig, ax = plt.subplots()
# scatterplot gdp as x, life-expectancy as y
plt.scatter(merged_entries[HEADER_TITLE_X], merged_entries[HEADER_TITLE_Y])
plt.xlabel(args.column_x)
plt.ylabel(args.column_y)

if args.output is not None:
    plt.savefig("../fig/" + args.output + ".png")
else:
    plt.show()
