# Tian Xiaoyang
# 26001904581
# week 10 Exercise

import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.twodim_base import _trilu_indices_form_dispatcher

def sigmoid(x): # define an activation sigmoid function
    return 1/(1 + np.exp(-x))

def sigmoidSlope(x): # define how to calculate the slope of the avtivation sigmoid function
    return x * (1 - x)

np.random.seed(1)
weights01 = 2*np.random.random((3,1))-1 # weights for the neural network
inputData = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]]) # the initial input data
referenceData = np.array([[0,0,1,1]]).T # desired output data, which will be used as reference for training in backporpagation algorithm

training_num = 50000 #set a number for the training iterations

for i in range(training_num): # backpropagation
    inputLayer = inputData # assign the input data array to the input layer
    outputPerceptronLayer = sigmoid(10*(np.dot(inputLayer, weights01))) # get the output perceptron layer by feeding the product of input data and weights to the sigmoid function
    outputError = referenceData - outputPerceptronLayer # the error between actual output and desired output
    outputDelta = outputError * sigmoidSlope(outputPerceptronLayer) # feed the output perceptron layer to sigmoid slope function, and assign the product of the function's outcome and the errors to the output delta
    weights01 += np.dot(inputLayer.T, outputDelta) # update the weights
    output_error_mean = np.mean(np.abs(outputError)) #calculate the mean of output errors
    out_rounded = np.round(outputPerceptronLayer, decimals = 2) # round the output to 2 decimals after the decimal dot
    if np.array_equal(referenceData, out_rounded): # compare the actual output and the desired one
        print("The output and the reference are equal")
        break

print("Output values after " + str(i) + " training iterations")
print(out_rounded)
print("Mean of output errors is \n"+ str(output_error_mean))
print("Output layer error is\n" + str(outputError))