import numpy as np

class NN:

    def sig(self,x):
        shiftx = x - np.max(x)
        return 1/(1+np.exp(-shiftx))
        #return 1/(1+np.exp(-x))

    def sigprime(self,x):
        return self.sig(x)*(1-self.sig(x))

    def soft(self,x):
        shiftx = x - np.max(x)
        exps = np.exp(shiftx)
        return exps / np.sum(exps)

    def softprime(self,x,row):
        s = x.reshape(-1,1)
        jacobian = (np.diagflat(s) - np.dot(s, s.T))
        rowone=jacobian[row,:]
        rowone=np.reshape(rowone,(1,-1))
        return rowone

    def __init__(self,In,Hn,On):
        self.inputneurons=In
        hiddenneurons=Hn
        outputneurons=On
        self.input=np.random.uniform(0,1,(1,self.inputneurons))
        self.l1w=np.random.uniform(0,1,(self.inputneurons,hiddenneurons))
        self.l2w=np.random.uniform(0,1,(hiddenneurons,outputneurons))
        print("weights1")
        print(self.l1w)
        print("weights2")
        print(self.l2w)

    def feedforward(self,x):
        self.input=x
        layer1=self.sig(np.dot(self.input,self.l1w))
        return self.soft(np.dot(self.sig(np.dot(self.input,self.l1w)),self.l2w))

    def addw1(self,x):
        self.l1w+=x

    def addw2(self,x):
        self.l2w+=x

    def dw2(self,row):
        layer1=self.sig(np.dot(self.input,self.l1w))
        leftSide=self.softprime(np.dot(layer1,self.l2w),row).T
        rightSide=layer1
        return np.dot(leftSide,rightSide).T

    def dw1(self,row):
        layer1=self.sig(np.dot(self.input,self.l1w))
        leftSide=np.dot(np.dot(self.input.T,self.softprime(np.dot(layer1,self.l2w),row)),self.l2w.T).T
        rightSide=self.sigprime(np.dot(self.input,self.l1w)).T
        return np.multiply(leftSide,rightSide).T

testInput=np.array([[0.9]])
wrt=50
print("input")
print(testInput)
newNN=NN(1,50,100)
print("output")
print(newNN.feedforward(testInput))

for x in range(1000):
    newNN.addw1(newNN.dw1(wrt))

    newNN.addw2(newNN.dw2(wrt))

print("output")
print(newNN.feedforward(testInput))
print("d1")
print(newNN.dw1(wrt))
print("d2")
print(newNN.dw2(wrt))
