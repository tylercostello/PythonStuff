#https://github.com/stephencwelch/Neural-Networks-Demystified/blob/master/Part%204%20Backpropagation.ipynb

import numpy as np
class Neural_Network(object):
    def __init__(self):
        #Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 4
        self.hiddenLayerSize = 3

        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)

    def forward(self, X):
        #Propogate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))

    def sigmoidPrime(self,z):
        #Gradient of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)

    def gradient(self, X, wtr):
        #Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)

        delta3 = self.sigmoidPrime(self.z3)
        dJdW2 = np.dot(self.a2.T, delta3)

        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)

        wtrarray=np.ones((self.inputLayerSize,self.hiddenLayerSize))
        wtrarray[wtr]=-1
        dJdW1=np.multiply(dJdW1,wtrarray)
        wtrarray=np.ones((self.hiddenLayerSize,self.outputLayerSize))
        wtrarray[:,wtr]=-1
        dJdW2=np.multiply(dJdW2,wtrarray)

        return dJdW1, dJdW2

    def addW1(self,x):
        self.W1+=x

    def addW2(self,x):
        self.W2+=x

nn = Neural_Network()
print(nn.forward(np.array([[1,2]])))
print(nn.gradient(np.array([[1,2]]),1))


for i in range (1000):
    if (i%100==0):
        print(nn.forward(np.array([[1,2]])))
    a,b=nn.gradient(np.array([[1,2]]),1)
    nn.addW1(a)
    nn.addW2(b)
