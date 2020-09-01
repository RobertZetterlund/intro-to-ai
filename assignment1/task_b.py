import numpy as np
import pandas as pd

SELECTED_YEAR = 2010
TITLE_OF_RELEVANT_DATA = 'Life expectancy (years)'

df = pd.read_csv('life-expectancy.csv')

# Extract data entries from dataframe where year is SELECTED YEAR, essentially filter
life_exp_list = df[(df['Year'] == SELECTED_YEAR)]

# Calculate standard deviation and mean
life_std = np.std(life_exp_list[TITLE_OF_RELEVANT_DATA])
life_mean = np.mean(life_exp_list[TITLE_OF_RELEVANT_DATA])

# get countries one mean above average
top_percentage_countries = life_exp_list[life_exp_list[TITLE_OF_RELEVANT_DATA] > life_mean+life_std]

#print countires being one std above the mean
print(top_percentage_countries['Entity'])