from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, GaussianNoise
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.regularizers import l2

from general import generateData, train_model



num_classes = 10

#generate data
(x_train, y_train,x_test, y_test, input_shape) = generateData(num_classes)

#Train model for different l_2 regularization parameters
for regParam in [0.001, 0.005, 0.01, 0.05, 0.1]:
    model, fit_info = train_model(
        x_train, 
        y_train, 
        x_test, 
        y_test,
        [Flatten(),
        Dense(100, activation='relu', kernel_regularizer=l2(regParam)),
        Dense(num_classes, activation='softmax')],
    )
    #Print score
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Reg param:",regParam,"Test loss: {}, Test accuracy {}".format(score[0], score[1]))