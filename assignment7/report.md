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

 ### B)

 ![img](fig/Q1b.png)

<!--- Perhaps use bar chart instead? --->

## _Question 2_
### A)
![img](fig/Q2a.png)


### B)

To find the optimal learning rate, that is, the learning rate that yields the best accuarcy, we try learning rates in the interval between 0.001 and 1.0.

The results show that the optimal learning rate is approxiamtely 0.6, which yields an accuracy of around 97.89 %.  

### C)


## _Question 3_

### A)

We add the gaussian noise layer as the first hidden layer, see code snippet below. 


The reason we put it as the first hidden layer is because...

We calculate the different predicitions score using the different standard deviations.

- `0.1` yields a test accuracy of 0.9785000085830688
- `1` yields a test accuracy of 0.9577000141143799
- `10` yields a test accuracy of 0.09740000218153


Can you come up with an argument for why adding noise like this could be a good idea in certain situations?

### B)
Reg param: 0.001 Test loss: 0.12269703298807144, Test accuracy 0.9768000245094299
Reg param: 0.005 Test loss: 0.1834477186203003, Test accuracy 0.9671000242233276
Reg param: 0.01 Test loss: 0.2412899136543274, Test accuracy 0.955299973487854
Reg param: 0.05 Test loss: 0.4854423701763153, Test accuracy 0.8988000154495239
Reg param: 0.1 Test loss: 0.9878652095794678, Test accuracy 0.7328000068664551


## _Question 4_

## A)

## B) 

One benefit of convolutional networks over fully connected is that they still can classify an image even though the image have been slightly shifted.

When shifting all the images in the validation dataset 3 pixels to the rigth, we get that the convolutional network performs a lot better than the fully connected network. 

- Convolutional network: 90.1 % accuracy
- Fully connected network 57.1 % accuracy


Another benfit of using convolutional networks is that there will be less parameters. This makes it more efficient when it comes memory and complexity. 
