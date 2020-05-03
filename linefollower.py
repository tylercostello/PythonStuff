#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import numpy as np
import random
# Each row is a training example, each column is a feature  [X1, X2, X3]

#generate array of inputs
inputArray=np.zeros((10,1),dtype=float)
#a=np.array([[]])
for b in range(10):
    a=np.zeros((1,1),dtype=float)
    for c in range (1):
        a[0][c]=random.uniform(0,0.7)
        #a=np.append(a,random.uniform(0,0.7))
    inputArray[b]=a
print(inputArray)


#generate array of outputs
outputArray=np.zeros((10,1),dtype=float)
for d in range (len(inputArray)):
    if (inputArray[d][0]<0.35):
        outputArray[d][0]=0
    else:
        outputArray[d][0]=1
print(outputArray)

X=inputArray
y=outputArray
#X=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]), dtype=float)
#y=np.array(([0],[1],[1],[0]), dtype=float)

# Define useful functions

# Activation function
def sigmoid(t):
    return 1/(1+np.exp(-t))

# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)

# Class definition
class NeuralNetwork:
    def __init__(self, x,y):
        self.input = x
        #print(self.input)
        #print(self.input.shape[1])
        self.weights1= np.random.rand(1,4)
        #self.weights1= np.random.rand(self.input.shape[1],4) # considering we have 4 nodes in the hidden layer
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np. zeros(y.shape)
    def setInput(self,x):
        self.input=x
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2

    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2*(self.y -self.output)*sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2*(self.y -self.output)*sigmoid_derivative(self.output), self.weights2.T)*sigmoid_derivative(self.layer1))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, y):
        self.output = self.feedforward()
        self.backprop()


NN = NeuralNetwork(X,y)
for i in range(1500): # trains the NN 1,000 times
    if i % 100 ==0:
        print ("for iteration # " + str(i) + "\n")
        #print ("Input : \n" + str(X))
        #print ("Actual Output: \n" + str(y))
        #print ("Predicted Output: \n" + str(NN.feedforward()))
        print ("Loss: \n" + str(np.mean(np.square(y - NN.feedforward())))) # mean sum squared loss
        print ("\n")

    NN.train(X, y)
newX=np.array(([0.1]), dtype=float)
NN.setInput(newX)
print(NN.feedforward())
newX=np.array(([0.6]), dtype=float)
NN.setInput(newX)
print(NN.feedforward())
