import numpy as np

class NN:

    def sig(self,x):
        #print(x)
        shiftx = x - np.max(x)
        #np.clip(shiftx,-10,10)
        return 1/(1+np.exp(-shiftx))

        #return 1/(1+np.exp(-x))

    def sigprime(self,x):
        return self.sig(x)*(1-self.sig(x))



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
        #print(np.dot(self.sig(np.dot(self.input,self.l1w)),self.l2w))
        return self.sig(np.dot(self.sig(np.dot(self.input,self.l1w)),self.l2w))

    def addw1(self,x):
        self.l1w+=x
        #print(x)

    def addw2(self,x):
        self.l2w+=x

    def dw2(self):
        layer1=self.sig(np.dot(self.input,self.l1w))
        leftSide=self.sigprime(np.dot(layer1,self.l2w)).T
        rightSide=layer1
        return np.dot(leftSide,rightSide).T

    def dw1(self):
        layer1=self.sig(np.dot(self.input,self.l1w))
        leftSide=np.dot(np.dot(self.input.T,self.sigprime(np.dot(layer1,self.l2w))),self.l2w.T).T
        rightSide=self.sigprime(np.dot(self.input,self.l1w)).T
        return np.multiply(leftSide,rightSide).T

testInput=np.array([[0.9]])

print("input")
print(testInput)
newNN=NN(1,2,2)
print("output")
print(newNN.feedforward(testInput))

for x in range(10000):
    newNN.feedforward(testInput)
    #print(10*newNN.dw1(wrt))
    newNN.addw1(0.01*newNN.dw1())
    newNN.addw2(0.01*newNN.dw2())


print("output")
print(newNN.feedforward(testInput))
print("d1")
print(newNN.dw1())
print("d2")
print(newNN.dw2())
