# Author: {Tobias Lindroth & Robert Zetterlund}
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import matplotlib.pyplot as plt

from general import generateData, train_model

import numpy as np
import math as m
from seaborn.matrix import heatmap
import pandas as pd
from matplotlib import cm

num_classes = 10
epochs = 10

# Generate the datasets
(x_train, y_train, x_test, y_test, _) = generateData(num_classes)

neuronsToTry = [10, 25, 50, 100, 150, 250, 500, 750, 1000]
learningRatesToTry = [0.001, 0.005, 0.01, 0.05, 0.1]

#Colors for plotting
colors = ["blue","red","green","orange","purple","cyan","pink","brown"]

#List to collect the performances of the different models
modelPerformances = []

for neurons in neuronsToTry:

    for lr in learningRatesToTry:
        # Train model
        model, fit_info = train_model(
            x_train,
            y_train,
            x_test,
            y_test,
            [
                Flatten(),
                Dense(neurons, activation='relu'),
                Dense(10, activation='softmax')],
            epochs=10,
            lr=lr
        )
        # Evalute accuracy
        accuracy = model.evaluate(x_test, y_test, verbose=0)[1]
        # Create model performance dict
        model_dict = {
                "neurons": neurons,
                "learning rate": lr,
                "accuracy": accuracy
        }
        # Add performance to list
        modelPerformances.append(model_dict)

        print(accuracy, "Neurons:", neurons, "Learning rate:", lr)

#Create a dataframe from model performances to make it easier to plot
df = pd.DataFrame(modelPerformances)

#Transform accuracy to percentage
df["accuracy"] = df["accuracy"]*100

#Get ax of figure
ax = plt.gca()

#Get list [0,1,2..... len(neuronsToTry)]
x = [neuron for neuron in range(len(neuronsToTry))]

for idx,lr in enumerate(learningRatesToTry):
    ## filter out learning rates for plot
    lr_df = df[df["learning rate"]==lr]
    ## used for equal spacing of x axis
    lr_df["x"] = x
    ## plot line
    lr_df.plot.line(x="x", y="accuracy", color=colors[idx], legend=True, marker='o', linewidth=2, ax=ax)

ax.legend(learningRatesToTry)

plt.title("Accuracies for different learning rates \n when the amount of neurons change ")
plt.ylabel("Accuracy (%)")
plt.xlabel("Number of neurons in layer")
plt.xticks(x, neuronsToTry)

plt.show()

## find best model and train it over 30 epochs

epochs = 30

bestModel = df.iloc[df['accuracy'].argmax()]
model, fit_info = train_model(
    x_train,
    y_train,
    x_test,
    y_test,
    [Flatten(),
     Dense(bestModel.at["neurons"], activation='relu'),
     Dense(10, activation='softmax')],
    epochs=epochs,
    lr=bestModel.at['learning rate']
)

# Plot a line chart
plt.plot(list(range(1, epochs+1)), [a*100 for a in fit_info.history['accuracy']],
         marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
plt.plot(list(range(1, epochs+1)), [a*100 for a in fit_info.history['val_accuracy']],
         marker='o', color='lime', markerfacecolor='green', markersize=8, linewidth=2)

# Fix y-ticks
last_val = fit_info.history['val_accuracy'][-1] * 100
min_val = min(fit_info.history["accuracy"]) * 100
range_start = 10 * (min_val//10) 
yticks = np.arange(range_start, 101, 10)
yticks = np.sort(np.append(yticks, last_val))
plt.yticks(yticks)

#Print dashed line for optimal value
plt.axhline(last_val, ls="--", c="k")

plt.legend(['Training dataset', 'Validation dataset'])
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
title = "Performance per epoch for " + \
    str(int(bestModel["neurons"])) + " number of neurons"
plt.title(title)
plt.show()