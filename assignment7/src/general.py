from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np
import random



### Method that trains a model 
# Returns the model and fit info
def train_model(x_train, y_train, x_val, y_val, layers, batch_size=128, num_classes=10, epochs=30, lr=0.1):

    ## Define model ##
    model = Sequential(layers)
    
    model.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.SGD(lr = lr),
                metrics=['accuracy'])


    fit_info = model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            verbose=1,
            validation_data=(x_val, y_val))


    return (model, fit_info)  



def generateData(num_classes, rollDirection=0, steps=0):
    # input image dimensions
    img_rows, img_cols = 28, 28

    # the data, split between train and test sets
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    #Roll image
    if rollDirection in [1,2,3,4]:
        imageToDisplay = random.randint(0, len(x_test)-1)
        displayImage(x_test[imageToDisplay])
        x_test = np.array([roll(matrix,rollDirection,steps) for matrix in x_test])
        displayImage(x_test[imageToDisplay])

    if K.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
        x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255  

    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)    


    return (x_train, y_train, x_test, y_test, input_shape)   


 
 

def roll(data, direction, steps):
    #rigth
    if direction == 1:
        return np.roll(data,steps,axis=1)  
    #left    
    elif direction == 2:
        return np.roll(data,-1*steps,axis=1)
    # UP
    elif direction == 3:
        return np.roll(data, -1*steps,axis = 0)
    # Down    
    elif direction == 4:
        return np.roll(data,steps,axis = 0)
        

def displayImage(image):
    np.array(image, dtype='float')
    pixels = image.reshape((28, 28))
    plt.imshow(pixels, cmap='gray')
    plt.show()