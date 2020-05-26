import numpy as np
import warnings

warnings.simplefilter(action = "ignore", category = RuntimeWarning)
class NN:
    def sig(self,x):
        return np.nan_to_num(1/(1+np.exp(-x)))
    def sigprime(self,x):
        return np.nan_to_num(self.sig(x)*(1-self.sig(x)))

    def soft(self,x):

        return np.nan_to_num(np.exp(x)/np.sum(np.exp(x)))

    def softprime(self,x):
        s = x.reshape(-1,1)
        #print(x.shape)
        #print((np.diagflat(s) - np.dot(s, s.T)).shape)
        jacobian = (np.diagflat(s) - np.dot(s, s.T))
        #print(jacobian.shape)
        rowone=jacobian[0,:]

        rowone=np.reshape(rowone,(1,-1))

        sum=jacobian.sum(axis=1)
        sum=np.reshape(sum,(1,-1))
        diag=np.diag(jacobian,k=0)
        diag=np.reshape(diag,(1,-1))
        #print(rowone.shape)
        #print(rowone)
        #column=np.zeros((len(jacobian),1))
        #print(len(jacobian))
        #for counter in range(len(jacobian)):
            #print(jacobian[counter:].sum())
        #    column[counter]=(jacobian[counter:].sum())/len(jacobian)
        #return column.T
        return np.nan_to_num(rowone)
        #return sum
        #return diag

        #return self.soft(x)*(1-self.soft(x))
    def __init__(self,In,Hn,On):
        self.inputneurons=In
        hiddenneurons=Hn
        outputneurons=On
        self.input=np.random.uniform(-1,1,(1,self.inputneurons))
        self.l1w=np.random.uniform(-1,1,(self.inputneurons,hiddenneurons))
        self.l2w=np.random.uniform(-1,1,(hiddenneurons,outputneurons))
        print("weights1")
        print(self.l1w)
        print("weights2")
        print(self.l2w)
    def feedforward(self,x):
        self.input=x
        #print(self.input)
        layer1=self.sig(np.dot(self.input,self.l1w))
        return np.nan_to_num(self.soft(np.dot(self.sig(np.dot(self.input,self.l1w)),self.l2w)))
    def addw1(self,x):
        self.l1w+=x
    def addw2(self,x):
        self.l2w+=x
    def dw2(self):
        layer1=self.sig(np.dot(self.input,self.l1w))
        return np.nan_to_num(np.dot(self.softprime(np.dot(layer1,self.l2w)).T,layer1).T)
    def dw1(self):
        layer1=self.sig(np.dot(self.input,self.l1w))
        return np.nan_to_num(np.multiply(np.dot(np.dot(self.input.T,self.softprime(np.dot(layer1,self.l2w))),self.l2w.T).T,self.sigprime(np.dot(self.input,self.l1w)).T).T)
testInput=np.array([[0.2]])
print("input")
print(testInput)
newNN=NN(1,2,3)
print("output")
#print(newNN.feedforward(np.array([[-0.5,-0.5]])))
print(newNN.feedforward(testInput))
for x in range(10000):
    newNN.addw1(0.01*newNN.dw1())
    #newNN.addw2(newNN.dw2())
    #w2adder=0.01*newNN.dw2()
    #w2adder[:,0]*=-1
    #w2adder[:,1]*=-1
    #newNN.addw2(w2adder)
    newNN.addw2(0.01*newNN.dw2())
    #newNN.feedforward(np.array([[-0.5,-0.5]]))
    newNN.feedforward(testInput)




print("output")
#print(newNN.feedforward(np.array([[-0.5,-0.5]])))
print(newNN.feedforward(testInput))
print("d1")
print(newNN.dw1())
print("d2")
print(newNN.dw2())
