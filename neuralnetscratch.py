import numpy as np

# Each row is a training example, each column is a feature  [X1, X2, X3]
#X=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]), dtype=float)
#y=np.array(([0],[1],[1],[0]), dtype=float)
X=np.array(([0,0,1]), dtype=float)
y=np.array(([0]), dtype=float)
# Define useful functions

# Activation function
def sigmoid(t):
    return 1/(1+np.exp(-t))
def relu(t):
    return t*(t>0)
# Derivative of sigmoid

# Class definition
class NeuralNetwork:
    def __init__(self, x,y):
        self.input = x
        self.weights1= np.random.rand(3,4)#3,4 # considering we have 4 nodes in the hidden layer
        self.biases1=np.random.rand(4)
        self.weights2 = np.random.rand(4,1) #4,1
        self.biases2=np.random.rand(1)
        self.y = y
        self.output = nzeros(y.shape)

    def setInput(self,x):
        self.input=x

    def feedforward(self):
        print(self.input)
        #print(relu(np.dot(self.input, self.weights1)))
        self.layer1 = relu(np.dot(self.input, self.weights1)+self.biases1)
        print(self.layer1)
        #print(self.biases1)
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2)+self.biases2)
        #print(self.biases1)
        print(self.layer2)
        return self.layer2
    def printWeights(self):
        print(self.weights1)
        print(self.weights2)
    def printBiases(self):
        print(self.biases1)
        print(self.biases2)
NN = NeuralNetwork(X,y)
#
NN.feedforward()

newX=np.array(([1,1,1]), dtype=float)
NN.setInput(newX)
NN.feedforward()
#NN.printBiases()
#NN.printWeights()
