## Author: {Tobias Lindroth & Robert Zetterlund}

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../res/data.csv")

x_header = "area"
y_header = "price"

# C

# Draw a residual plot

# select regression model
reg = LinearRegression()

# extract x and y and create regression fit
x = df[x_header].values.reshape(-1, 1)
y = df[y_header].values.reshape(-1, 1)
reg.fit(x, y)

# use regression fit to get predicted y values. 
y_predicted = reg.predict(x)
# calculate residuals
residuals = y-y_predicted

# The r2 score of the correlation
print('score: ', reg.score(x, y))

# setup plot
fig, ax = plt.subplots()
plt.ylim(-2000000, 2000000)
plt.xlabel(x_header)
plt.ylabel("Residuals")

# scatterplot residuals
plt.plot(x, residuals, 'o', alpha=0.9)
# create horizontal line to show the prediction of the linear regression 
plt.axhline(y=0, ls="--", alpha=0.7, color="black")

plt.show()

# D
# d. Discuss the results, and how the model could be improved.


# Regarding the results.
#   our R-squared "score" is 0.543,
#


# More datapoints
# There are more factors to take into account
# Area of land in measurements
# Year of building the house
# Is it newly renovated?
# Do we have additional living space? (biarea)
# What is the annual cost of keeping the property?
# Where is it located? Near city centre or not?
