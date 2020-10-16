# Assignment 7

### Tobias Lindroth: x hrs

### Robert Zetterlund: y hrs

## _Question 1_

### _A)_

The layers are created in this sequence of code

```python

model.add(Dense(125, activation = 'relu'))
model.add(Dense(100, activation = 'relu'))
model.add(Dense(50, activation = 'relu'))
model.add(Dense(num_classes, activation='softmax'))

```

Which results in

- 1 input layer
- 3 hidden layers
- 1 output layer

In total: **`5`** layers.

Where

- Input layer has 28\*28=`784` neurons
- Hidden layer 1 has `125` neurons
- Hidden layer 2 has `100` neurons
- Hidden layer 3 has `50` neurons
- Output layer has `10` neurons

The parameters in the network are weights and biases.

The total number of weights (the number of connections between the neurons), are:

```
784*125 + 125*100 + 100*50 + 50*10 = 116000
```

The total number of biases (the number of nodes) are:

```
125 + 100 + 50 + 10 = 285
```

In total, the network has 116000+285 = 116285 parameters.

We can verify this by using the `summary()`-method that is available for keras-models.

```python
print(model.summary())


Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
flatten (Flatten)            (None, 784)               0
_________________________________________________________________
dense (Dense)                (None, 125)               98125
_________________________________________________________________
dense_1 (Dense)              (None, 100)               12600
_________________________________________________________________
dense_2 (Dense)              (None, 50)                5050
_________________________________________________________________
dense_3 (Dense)              (None, 10)                510
=================================================================
Total params: 116,285
Trainable params: 116,285
Non-trainable params: 0

```

### B)

```python
# get fit_info when training model
fit_info = model.fit(...)

# Plot test-accuracy
plt.plot( list(range(1,epochs+1)), [a*100 for a in fit_info.history['accuracy']], marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
# Plot validation-accuracy.
plt.plot( list(range(1,epochs+1)), [a*100 for a in fit_info.history['val_accuracy']], marker='o', color='olive',markersize=8, linewidth=2)
```

![img](fig/Q1b.png)

<!--- Perhaps use bar chart instead? --->

## _Question 2_

### A)

Similar as before, the learning rate is set to 0.1, and the layers of the model is:

```python
[
    Flatten(),
    Dense(100, activation='relu'),
    Dense(10, activation='softmax')
]
```

![img](fig/Q2a.png)

### B)

To find the optimal learning rate, that is, the learning rate that yields the best accuarcy, we try learning rates in the interval between 0.001 and 1.0.

```python
learningrates = [0.001, 0.005, 0.025, 0.05, 0.1, 0.25, 0.5, 1]

for learningRate in learningrates:
    for j in range(3):
        # train model, store accuracy, learning rate
        train_model(...,lr=learningRate)

        accuracy += model.evaluate(x_test, y_test, verbose=0)[1]

    #calculate accuracy average
    accuracy /= 3
    # Add learning rate and the average accuracy to the list
    accuracies.append((learningRate,accuracy))


# get highest avg
bestAccuracy = max(accuracies, key=lambda item:item[1])
```

The results show that the optimal learning rate is approxiamtely 0.5, which yields an accuracy of 0.978 %.

### C)

## _Question 3_

### A)

We add the gaussian noise layer as the first hidden layer, see code snippet below.

```python
[
    Flatten(),
    GaussianNoise(<standardDeviation>),
    Dense(100, activation='relu'),
    Dense(num_classes, activation='softmax')
]
```

We use simple for loop and iterate over suggested standardDeviations.

```python
for standardDeviation in [0.1,1,10]:
    # train and evaluate model
```

We calculate the different predicitions score using the different standard deviations.

- `0.1` yields a test accuracy of 0.9785000085830688
- `1` yields a test accuracy of 0.9577000141143799
- `10` yields a test accuracy of 0.09740000218153

**Can you come up with an argument for why adding noise like this could be a good idea in certain situations?**

The reason we put Gaussian noise as the first hidden layer is because of the consensus within the community.

According to [Jason Brownlee PhD](https://machinelearningmastery.com/train-neural-networks-with-noise-to-reduce-overfitting/), Gaussian noise can be useful to reduce overfitting. [to be continued]

### B)

| reg param | Test loss | Test accuracy |
| --------- | --------- | ------------- |
| 0.001     | 0.12269   | 0.9768        |
| 0.005     | 0.18344   | 0.9671        |
| 0.01      | 0.24128   | 0.9552        |
| 0.05      | 0.48544   | 0.8988        |
| 0.001     | 0.98786   | 0.7328        |

<!--Reg param: 0.001 Test loss: 0.12269703298807144, Test accuracy 0.9768000245094299
Reg param: 0.005 Test loss: 0.1834477186203003, Test accuracy 0.9671000242233276
Reg param: 0.01 Test loss: 0.2412899136543274, Test accuracy 0.955299973487854
Reg param: 0.05 Test loss: 0.4854423701763153, Test accuracy 0.8988000154495239
Reg param: 0.1 Test loss: 0.9878652095794678, Test accuracy 0.7328000068664551
-->

## _Question 4_

### A)

<!--
Use at least one convolutional layer and try and create a network that can reach 99% accuracy on the validation data. If you choose to use any layers except convolutional layers and layers that you used in previous exercises, you must describe what they do. If you do not reach 99% accuracy, report your best performance and explain your attempts and thought process.
 -->

```python
 [
    GaussianNoise(0.1),
    Conv2D(30, (5,5), activation="relu", input_shape=input_shape, kernel_regularizer=l2(0.001)),
    MaxPooling2D(2,2),
    Conv2D(60,(5,5), activation="relu", input_shape=input_shape, kernel_regularizer=l2(0.001)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(num_classes, activation='softmax')
]
```

### B)

<!--
What is a benefit of using convolutional layers over fully connected ones?



--->
