import matplotlib.pyplot as plt
import numpy as np
import csv

SELECTED_YEAR = '2010'
life_expectancy_dict = {}
gdp_dict = {}


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

print(int(np.std(gdp_array)))
print(int(np.std(life_array)))

print(int(np.var(gdp_array)))
print(int(np.var(life_array)))


# create plot
fig, ax = plt.subplots()
plt.scatter(gdp_array, life_array)

# show plot
plt.show()
