from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../res/data.csv")


x_header = "area"
y_header = "price"

# C
# Draw a residual plot
x = df[x_header].values.reshape(-1, 1)
y = df[y_header].values.reshape(-1, 1)
reg = LinearRegression()

reg.fit(x, y)
y_predicted = reg.predict(x)
residuals = y-y_predicted


fig, ax = plt.subplots()

plt.plot(x, residuals, 'o', alpha=0.9)
plt.ylim(-2000000, 2000000)
plt.xlabel(x_header)
plt.ylabel("Residuals")

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
