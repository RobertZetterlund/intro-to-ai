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
epochs = 5

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
