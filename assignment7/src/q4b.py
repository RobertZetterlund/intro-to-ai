# Use at least one convolutional layer and try and create a network that can reach 99% accuracy 
# on the validation data. If you choose to use any layers except convolutional layers and layers 
# that you used in previous exercises, you must describe what they do. 
# If you do not reach 99% accuracy, report your best performance and explain your attempts and thought process.


from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, GaussianNoise
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.regularizers import l2
import numpy as np

from general import generateData, train_model


num_classes = 10

#generate data
(x_train, y_train,x_test, y_test, input_shape) = generateData(num_classes, 1,3)


#Train model

convModel, _ = train_model(
    x_train, 
    y_train, 
    x_test, 
    y_test,
    [
    GaussianNoise(0.1),
    Conv2D(45, (5,5), activation="relu", input_shape=input_shape, kernel_regularizer=l2(0.001)),
    MaxPooling2D(2,2),
    Conv2D(60,(5,5), activation="relu", input_shape=input_shape),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(num_classes, activation='softmax')
    ],
)

model, _ = train_model(
    x_train, 
    y_train, 
    x_test, 
    y_test,
    [Flatten(), 
     Dense(100, activation='relu'), 
     Dense(10, activation='softmax')]
    )
convScore = convModel.evaluate(x_test, y_test, verbose=0)
print("Convolutional network: Test loss: {}, Test accuracy {}".format(convScore[0], convScore[1]))   
score = model.evaluate(x_test, y_test, verbose=0)
print("Fully connected network: Test loss: {}, Test accuracy {}".format(score[0], score[1]))


print(convModel.summary())
print(model.summary())



