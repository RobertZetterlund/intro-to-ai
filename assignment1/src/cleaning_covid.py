
import pandas as pd

SELECTED_DATE = '2020-08-31'
df = pd.read_csv('../res/owid-covid-data.csv')


entries = df[(df['date'] == SELECTED_DATE)]

entries = entries[['location','total_deaths_per_million']].dropna()

entries.to_csv('../res/clean_covid.csv', index=False)