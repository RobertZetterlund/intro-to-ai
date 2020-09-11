## Author: {Tobias Lindroth & Robert Zetterlund}

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../res/data.csv")

x_header = "area (m2)"
y_header = "price (SEK)"

# A
# What are the values of the slope and intercept of the regression line?
x = df[x_header].values.reshape(-1, 1)
y = df[y_header].values.reshape(-1, 1)
reg = LinearRegression()

reg.fit(x, y)

slope = reg.coef_
intercept = reg.intercept_

print("reg.coef_: ", slope)
print("reg.intercept_:", intercept)

# B
# Use this model to predict the selling prices of houses which have living area 100 m2 , 150 m2 and 200 m2

print("predicted value of house with 100m2 =", 100 * slope + intercept)
print("predicted value of house with 150m2 =", 150 * slope + intercept)
print("predicted value of house with 200m2 =", 200 * slope + intercept)

## Setup plot
fig, ax = plt.subplots()
plt.xlabel(x_header)
plt.ylabel(y_header)
plt.ylim(np.amin(y)-100000, np.amax(y)+100000)
plt.xlim(np.amin(x)-10, np.amax(x)+10)

# draw regression line
x_predicted = np.linspace(0, np.amax(x)+50).reshape(-1,1)
def f(x): return reg.predict(x)
plt.plot(x_predicted, f(x_predicted), c="red")

# create scatterplot
plt.scatter(x, y)

plt.show()


