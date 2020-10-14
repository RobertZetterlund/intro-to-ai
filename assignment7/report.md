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

To find the optimal learning rate, that is, the learning rate that yields the best accuarcy, we tried learning rates in the interval between 0.001 and 1.0 with a step length of 0.05. 

The results show that the optimal learning rate is approxiamtely 0.6, which yields an accuracy of around 97.89 %.  

### C)
