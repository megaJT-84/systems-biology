# Tian Xiaoyang
# 26001904581
# week 10 Exercise

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x): # define an activation sigmoid function
    return 1/(1 + np.exp(-x))

def sigmoidSlope(x): # define how to calculate the slope of the avtivation sigmoid function
    return x * (1 - x)

training_number = 900 #set training iterations
inputData = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]]) # the initial input data
output_referenceData_w10 = np.array([[0,0,1,1]]).T # desired output data for single alyer NN, which will be used as reference for training in backporpagation algorithm
output_referenceData_w11 = np.array([[0,1,1,0]]).T # desired output data for multi alyer NN, which will be used as reference for training in backporpagation algorithm
iter = np.empty(900) # an array of numbers from 1 to 900, for the iteration number in the graph
for i in range (training_number):
    iter[i] = str(i)

def singleLayer_NN(inputdata, output_referenceData, training_no):
    np.random.seed(42)
    weights01 = 2*np.random.random((3,1))-1 # weights for the neural network
    singleNN_output_layer = np.empty(900)#create an empty array for output errors
    for i in range(training_no): # backpropagation
        inputLayer = inputdata # assign the input data array to the input layer
        
        outputPerceptronLayer = sigmoid(np.dot(inputLayer, weights01)) # get the output perceptron layer by feeding the product of input data and weights to the sigmoid function
        
        outputError_single = output_referenceData - outputPerceptronLayer # the error between actual output and desired output
        
        outputDelta = outputError_single * sigmoidSlope(outputPerceptronLayer) # feed the output perceptron layer to sigmoid slope function, and assign the product of the function's outcome and the errors to the output delta
        
        weights01 += np.dot(inputLayer.T, outputDelta) # update the weights
        
        singleNN_output_layer[i] = np.mean(np.abs(outputError_single)) #calculate the mean of output errors, put them in the array
        
        out_rounded = np.round(outputPerceptronLayer, decimals=2) # round the output to 2 decimals after the decimal dot
    print("output values after " + str(i) + " training iterations:")
    print(out_rounded)
    print("mean value of output errors is: ")
    print(str(np.round(singleNN_output_layer)))

    return singleNN_output_layer

def multiLayer_NN(inputdata, output_referenceData, training_no):
    np.random.seed(42)
    weights01 = 2*np.random.random((3,4))-1 # weights for the neural network
    weights02 = 2*np.random.random((4,1))-1
    multiNN_output_layer = np.empty(900) #create an empty array for output errors
    for i in range(training_no): # backpropagation
        inputLayer = inputdata # assign the input data array to the input layer

        hidden_Layer= sigmoid(np.dot(inputLayer,weights01))#hidden layer is the dot procudt of weights01 and the input layer

        outputPerceptronLayer = sigmoid(np.dot(hidden_Layer, weights02)) # get the output perceptron layer by feeding the product of input data and weights to the sigmoid function

        outputError_multi = output_referenceData - outputPerceptronLayer # the error between actual output and desired output

        outputDelta = outputError_multi * sigmoidSlope(outputPerceptronLayer) # feed the output perceptron layer to sigmoid slope function, and assign the product of the function's outcome and the errors to the output delta

        hidden_Error = outputDelta.dot(weights02.T) # hidden layer error is the dot product of output layer delta and transposed weights02

        hidden_Delta = hidden_Error*sigmoidSlope(hidden_Layer)#hidden layer delta is the product of hidden layer error and the result from sigmoid slope function when hidden layer is fed into it

        weights02 += hidden_Layer.T.dot(outputDelta)# update weights02

        weights01 += inputData.T.dot(hidden_Delta) # update weights01

        out_rounded_multi = np.round(outputPerceptronLayer) # round the output to 2 decimals after the decimal dot

        multiNN_output_layer[i] = np.mean(np.abs(outputError_multi)) #calculate the mean of output errors
    print("output values after " + str(i) + " training iterations:")
    print(out_rounded_multi)
    print("mean value of output errors is:")
    print(str(multiNN_output_layer))
    return multiNN_output_layer

if __name__ == "__main__":

    single1 = singleLayer_NN(inputData, output_referenceData_w10, training_number) # assign output from single layer NN to a varaible
    single2 = singleLayer_NN(inputData, output_referenceData_w11, training_number)# assign output from single layer NN to a varaible
    multi1 = multiLayer_NN(inputData, output_referenceData_w10, training_number)# assign output from multi layer NN to a varaible
    multi2 = multiLayer_NN(inputData, output_referenceData_w11, training_number)# assign output from multi layer NN to a varaible

    plt.plot(single1, iter, color = "red") # plot the lines
    plt.plot(single2, iter, color = "yellow")
    plt.plot(multi1, iter, color = "blue")
    plt.plot(multi2, iter, color = "green")
    plt.xlabel('output error values')# x label is the output reference data
    plt.ylabel('iterations')# y label is the output errors' mean value
    plt.title("scatter plot for multilayer neural network") # graph title
    plt.show()#show the graph

