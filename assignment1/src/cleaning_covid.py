
import pandas as pd
import matplotlib.pyplot as plt

SELECTED_DATE = '2020-08-31'
df = pd.read_csv('../res/owid-covid-data.csv')


countryList = ["Sweden", "Norway", "Finland", "Denmark"]

entries = df[(df["location"].isin(countryList))]

entries = entries[(entries['date'].str.contains('2020-08'))]

entries = entries[['location', 'date', 'new_cases']]


def extract_data(country):
    return entries.loc[entries['location'] == country]['new_cases']


country_data = [extract_data(country) for country in countryList]


fig = plt.figure()
# Create an axes instance
ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot(country_data)
ax.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2], bp["boxes"][3]], countryList, loc='upper right')

plt.show()