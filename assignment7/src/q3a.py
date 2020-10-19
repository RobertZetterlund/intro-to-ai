# Author: {Tobias Lindroth & Robert Zetterlund}
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, GaussianNoise
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K


from general import generateData, train_model

num_classes = 10

#generate data
(x_train, y_train,x_test, y_test, input_shape) = generateData(num_classes)

#Train model for each standard deviation
for standardDeviation in [0.1,1,10]:
    model, fit_info = train_model(
        x_train, 
        y_train, 
        x_test, 
        y_test,
        [Flatten(),
        GaussianNoise(standardDeviation),
        Dense(100, activation='relu'),
        Dense(num_classes, activation='softmax')],
    )
    #Print the score
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Standard deviation", standardDeviation, "Test loss: {}, Test accuracy {}".format(score[0], score[1]))