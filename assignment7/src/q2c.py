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
#
#
num_classes = 10
epochs = 10
USE_OLD_DATA = False

# generate data
(x_train, y_train), (x_test, y_test) = generateData(num_classes)

neuronsToTry = [10, 150, 500]  # [10, 25, 50, 100, 150, 250, 500, 750, 1000]
#
learningRatesToTry = [0.001, 0.01, 0.1]  # [0.001, 0.005, 0.01, 0.05, 0.1]
# A list to collect the performance of the model depending
# on the number of neurons
modelPerformances = []

if(not USE_OLD_DATA):

    for neurons in neuronsToTry:

        for lr in learningRatesToTry:
            # Train model
            model, fit_info = train_model(
                x_train,
                y_train,
                x_test,
                y_test,
                [Flatten(),
                 Dense(neurons, activation='relu'),
                 Dense(10, activation='softmax')],
                epochs=10,
                lr=lr
            )
            # Evalute accuracy
            accuracy = model.evaluate(x_test, y_test, verbose=0)[1]

            model_dict = {
                "neurons": neurons,
                "learning rate": lr,
                "accuracy": accuracy
            }
            # Add performance to list
            modelPerformances.append(model_dict)

            print(accuracy, "Neurons:", neurons, "Learning rate:", lr)

    df = pd.DataFrame(modelPerformances)

# Create two subplots

# https://matplotlib.org/3.1.1/gallery/mplot3d/3d_bars.html

else:

    data = [
        [10, 0.001, 0.7530],
        [10, 0.010, 0.9030],
        [10, 0.100, 0.9359],
        [150, 0.001, 0.8630],
        [150, 0.010, 0.9253],
        [150, 0.100, 0.9714],
        [500, 0.001, 0.8684],
        [500, 0.010, 0.9295],
        [500, 0.100, 0.9721]
    ]

    df = pd.DataFrame(data, columns=["neurons", "learning rate", "accuracy"])


ax1 = df.plot.scatter(x="neurons", y="learning rate",
                      c="accuracy", colormap="winter")
ax1.set_xticks(neuronsToTry)
ax1.set_yticks(learningRatesToTry)
plt.show()

# Plot in some way


# Get best model
bestModel = df.iloc[df['accuracy'].argmax()]
model, fit_info = train_model(
    x_train,
    y_train,
    x_test,
    y_test,
    [Flatten(),
     Dense(bestModel.at["neurons"], activation='relu'),
     Dense(10, activation='softmax')],
    epochs=30,
    lr=bestModel.at['learning rate']
)
Plot a line chart
#fig, (ax1, ax2) = plt.subplots(1, 2)
plt.plot(list(range(1, 30+1)), [a*100 for a in fit_info.history['accuracy']],
         marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
plt.plot(list(range(1, 30+1)), [a*100 for a in fit_info["fit_info"].history['val_accuracy']],
         marker='o', color='olive', markersize=8, linewidth=2)


#ax1.title(str(bestModel[0]) + " neurons in hidden layer")
plt.legend(['Training dataset', 'Validation dataset'])
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
title = "Performance per epoch for " + \
    str(bestModel["neurons"]) + " number of neurons"
plt.title(title)
plt.show()
