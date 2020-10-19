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


num_classes = 10
epochs = 10

#generate data
(x_train, y_train,x_test, y_test, input_shape) = generateData(num_classes)

#list to collect the accuracies for different learning rates
accuracies = []

#what learning rates to iterate through
learningrates = [0.001, 0.005, 0.025, 0.05, 0.1, 0.25, 0.5, 1]


for learningRate in learningrates:
    accuracy = 0
    #3 times for each learning rate
    for j in range(3):
        #Train model
        model, fit_info = train_model(
        x_train, 
        y_train, 
        x_test, 
        y_test,
        [Flatten(),  
        Dense(100, activation='relu'), 
        Dense(10, activation='softmax')],
        epochs=10,
        lr=learningRate
        )
        #Evalute accuracy
        accuracy += model.evaluate(x_test, y_test, verbose=0)[1]
    #Calcualte accuracy average
    accuracy /= 3
    print("Learning rate:", learningRate, "Accuracy:", accuracy)
    # Add learning rate and the average accuracy to the list
    accuracies.append((learningRate,accuracy))

#Check which learning rate got the best accuracy
bestAccuracy = max(accuracies, key=lambda item:item[1])

print(bestAccuracy)

        
  