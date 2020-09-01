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
with open('gdp.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Year'] == SELECTED_YEAR:
            code = row['Code']
            gdp = float(
                row['Output-side real GDP per capita (2011 international-$)'])
            gdp_dict[code] = gdp

print(life_expectancy_dict)
print(gdp_dict)


gdp_list = []
life_list = []

# add to arrays to plot
for code in gdp_dict:
    gdp_list.append(gdp_dict[code])
    life_list.append(life_expectancy_dict[code])

gdp_array = np.array(gdp_list)
life_array = np.array(life_list)

life_std = np.std(life_array)
life_mean = np.mean(life_array)

life_array_top_60 = life_array[life_array > life_mean+life_std]

print(life_array_top_60)
print(int(np.std(gdp_array)))
print(int(np.std(life_array)))

# create plot
fig, ax = plt.subplots()
plt.scatter(gdp_array, life_array)

# show plot
plt.show()
