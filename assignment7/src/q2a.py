from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np

from general import generateData, train_model

# Set values of learning rates and neurons in layer
learning_rate = 0.1
neurons_in_layer = 100

num_classes = 10
epochs = 30
# Generate the data
(x_train, y_train, x_test, y_test, _) = generateData(num_classes)

title = "Accuracies for neural net, lr=" + \
    str(learning_rate) + " neurons=" + str(neurons_in_layer)
print(title)

# Train the model
model, fit_info = train_model(
    x_train,
    y_train,
    x_test,
    y_test,
    [Flatten(),
     Dense(100, activation='relu'),
     Dense(10, activation='softmax')], lr=learning_rate, epochs=epochs
)

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss: {}, Test accuracy {}".format(score[0], score[1]))

# Plot a line chart
plt.plot(list(range(1, epochs+1)), [a*100 for a in fit_info.history['accuracy']],
         marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
plt.plot(list(range(1, epochs+1)), [a*100 for a in fit_info.history['val_accuracy']],
         marker='o', color='lime', markerfacecolor='green', markersize=8, linewidth=2)


plt.title(title)

# Fix y-ticks
last_val = fit_info.history['val_accuracy'][-1] * 100
min_val = min(fit_info.history["accuracy"]) * 100
range_start = 10 * (min_val//10) 
yticks = np.arange(range_start, 101, 10)
yticks = np.sort(np.append(yticks, last_val))
plt.yticks(yticks)

#Print dashed line for optimal value
plt.axhline(last_val, ls="--", c="k")

#Legend and labels
plt.legend(['Training dataset', 'Validation dataset'], loc="lower right")
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
#Show the plot
plt.show()
