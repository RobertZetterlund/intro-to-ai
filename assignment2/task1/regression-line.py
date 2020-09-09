from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")


x_header = "area"
y_header = "price"

## A
## What are the values of the slope and intercept of the regression line?
x = df[x_header].values.reshape(-1,1)
y = df[y_header].values.reshape(-1,1)
reg = LinearRegression()

reg.fit(x, y)

slope = reg.coef_
intercept = reg.intercept_

print("reg.coef_: ", slope)
print("reg.intercept_:", intercept)

## B
## Use this model to predict the selling prices of houses which have living area 100 m2 , 150 m2 and 200 m2

print("predicted value of house with 100m2 =", 100 * slope + intercept)
print("predicted value of house with 150m2 =", 150 * slope + intercept)
print("predicted value of house with 200m2 =", 200 * slope + intercept)

## C
## Draw a residual plot

y_predicted = reg.predict(x)
residuals = y-y_predicted

plt.plot(x, residuals, 'o', alpha=0.9)
#plt.plot(x, np.zeros(24), linestyle="--")


#fig, ax = plt.subplots()
# scatterplot gdp as x, life-expectancy as y
# #plt.scatter(x, y)

plt.xlabel(x_header)
plt.ylabel(y_header)
plt.axhline(y=0, ls="--", alpha=0.7, color="black")
#plt.hlines(y=0, xmin=np.amin(x), xmax=np.amax(x), linestyles='dashed', clipOn=False)

#plt.Line2D(x, x*slope + intercept)

plt.show()

## D
## d. Discuss the results, and how the model could be improved.