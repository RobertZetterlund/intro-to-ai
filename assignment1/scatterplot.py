import matplotlib.pyplot as plt
import numpy as np
import csv
import re  # Library for dealing with regular expressions
from functools import reduce

SELECTED_YEAR = '2010'
life_expectancy_dict = {}
gdp_dict = {}


# Given an array of numbers, calculate the average
def average(array):
    return np.sum(array)/(len(array))


def calcVar(array):
    avg = average(array)
    def deviation(acc, value): return acc + (value-avg)**2

    sum = reduce(deviation, array, 0)
    return sum / len(array)


def standard_deviation(array):
    variance = calcVar(array)
    return variance**(1/2)


# open life expectancy.csv, add values to life_expectancy dictionary
with open('life-expectancy.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Year'] == SELECTED_YEAR:
            code = row['Code']
            life_exp = float(row['Life expectancy (years)'])
            life_expectancy_dict[code] = life_exp

# open gdp per capita, add values to gdp dictionary
with open('real-gdp-per-capita-PWT.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Year'] == SELECTED_YEAR:
            code = row['Code']
            gdp = float(
                row['Output-side real GDP per capita (2011 international-$)'])
            gdp_dict[code] = gdp

print(life_expectancy_dict)
print(gdp_dict)


gdp_array = []
life_array = []

# add to arrays to plot
for code in gdp_dict:
    gdp_array.append(gdp_dict[code])
    life_array.append(life_expectancy_dict[code])

print(int(standard_deviation(gdp_array)))
print(int(standard_deviation(life_array)))

# create plot
fig, ax = plt.subplots()
plt.scatter(gdp_array, life_array)

# show plot
plt.show()
