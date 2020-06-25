#https://github.com/stephencwelch/Neural-Networks-Demystified/blob/master/Part%204%20Backpropagation.ipynb

import numpy as np
class Neural_Network(object):
    def __init__(self):
        #Define Hyperparameters
        self.inputLayerSize = 4
        self.outputLayerSize = 2
        self.hiddenLayerSize = 3

        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)

    def forward(self, X):
        #Propogate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.soft(self.z3)
        return yHat

    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))

    def sigmoidPrime(self,z):
        #Gradient of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)

    def soft(self,x):
        shiftx = x - np.max(x)
        #np.clip(shiftx,-10,10)
        exps = np.exp(shiftx)
        return exps / np.sum(exps)

    def softprime(self,x,row):
        s = x.reshape(-1,1)
        jacobian = (np.diagflat(s) - np.dot(s, s.T))
        returnrow=jacobian[row,:]
        returnrow=np.reshape(returnrow,(1,-1))
        return returnrow


    def costFunction(self, X, y):
        #Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)
        J = 0.5*sum((y-self.yHat)**2)
        return J

    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)

        delta3 = np.multiply((y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)


        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)


        return dJdW1, dJdW2
    def addW1(self,x):
        self.W1+=x
    def addW2(self,x):
        self.W2+=x

nn = Neural_Network()
#print(nn.forward(np.array([[1]])))
#print(nn.costFunctionPrime(np.array([[1]]),np.array([[0.2,0.8]])))

for i in range (1000):
    if (i%100==0):
        print(nn.forward(np.array([[1,3,1,4]])))
    actionarray=np.zeros((2))
    actionarray[0]=1
    #a,b=nn.costFunctionPrime(np.array([[1,3]]),np.array([[1,0]]))
    a,b=nn.costFunctionPrime(np.array([[1,3,1,4]]),actionarray)
    nn.addW1(a)
    nn.addW2(b)
