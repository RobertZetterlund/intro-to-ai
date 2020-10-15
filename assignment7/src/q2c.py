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

#generate data
(x_train, y_train), (x_test, y_test) = generateData(num_classes)







neuronsToTry = np.arange(10,1000, 100)
learningRatesToTry = np.linspace(0.05, 1, 20)
# A list to collect the performance of the model depending
# on the number of neurons
modelPerformances = []

for neurons in neuronsToTry :

    for lr in learningRatesToTry:
        #Train model
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
        #Evalute accuracy
        accuracy = model.evaluate(x_test, y_test, verbose=0)[1]

        # Add performance to list
        modelPerformances.append(
            {"neurons":neurons,
            "lr":lr,
            "acc":accuracy})
    
        print(accuracy, "Neurons:",neurons,"Learning rate:", lr)
    



#Create two subplots
fig, (ax1, ax2) = plt.subplots(1, 2)



#Plot in some way




#Get best model
bestModel = max(modelPerformances, key=lambda item:item["acc"])
model,fit_info = train_model(
        x_train, 
        y_train, 
        x_test, 
        y_test,
        [Flatten(),
        Dense(bestModel["neurons"], activation='relu'),
        Dense(10, activation='softmax')],
        epochs=30,
        lr=bestModel["lr"]
        )
#Plot a line chart
ax2.plot( list(range(1,epochs+1)), [a*100 for a in fit_info.history['accuracy']], marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
ax2.plot( list(range(1,epochs+1)), [a*100 for a in fit_info["fit_info"].history['val_accuracy']], marker='o', color='olive',markersize=8, linewidth=2)



#ax1.title(str(bestModel[0]) + " neurons in hidden layer")
ax2.legend(['Training dataset', 'Validation dataset'])
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Accuracy (%)")
title = "Performance per epoch for " + str(bestModel["neurons"]) + " number of neurons"
ax2.set_title(title)
plt.show()
  

        
  