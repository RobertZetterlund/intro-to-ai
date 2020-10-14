from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import matplotlib.pyplot as plt

from general import generateData, train_model

num_classes = 10
epochs = 30
#Generate the data 
(x_train, y_train), (x_test, y_test) = generateData(num_classes)

#Train the model
model, fit_info = train_model(
    x_train, 
    y_train, 
    x_test, 
    y_test,
    [Flatten(), 
     Dense(100, activation='relu'), 
     Dense(10, activation='softmax')]
    )

#Plot a line chart
plt.plot( list(range(1,epochs+1)), [a*100 for a in fit_info.history['accuracy']], marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
plt.plot( list(range(1,epochs+1)), [a*100 for a in fit_info.history['val_accuracy']], marker='o', color='olive',markersize=8, linewidth=2)


plt.legend(['Training dataset', 'Validation dataset'])
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
plt.show()
  