from scipy import stats
import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

x = df['price']
y = df['area']
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)


print("slope:", slope)
print("intercept:", intercept)