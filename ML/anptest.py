import autograd.numpy as np
from autograd import jacobian
from autograd import grad

def sig(x):
    return 1/(1+np.exp(-x))

def sigprime(x):
    return sig(x)*(1-sig(x))

myinput=np.array([[1]])
inputneurons=1
hiddenneurons=2
outputneurons=4

input=np.random.uniform(-1,1,(1,inputneurons))
l1w=np.random.uniform(-1,1,(inputneurons,hiddenneurons))
l2w=np.random.uniform(-1,1,(hiddenneurons,outputneurons))
"""
input=np.random.rand(1,inputneurons)
l1w=np.random.rand(inputneurons,hiddenneurons)
l2w=np.random.rand(hiddenneurons,outputneurons)
"""
layer1=sig(np.dot(input,l1w))
print("input")
print(myinput)
print("weights1")
print(l1w)
print("weights2")
print(l2w)
def feedforward(x):
    input=x
    layer1=sig(np.dot(input,l1w))
    return sig(np.dot(sig(np.dot(input,l1w)),l2w))
print("output")
print(feedforward(myinput))

def dw2():
    return np.dot(sigprime(np.dot(layer1,l2w)).T,layer1).T
def dw1():
    #return np.multiply(input,np.multiply(np.dot(sigprime(np.dot(layer1,l2w)),l2w.T),sigprime(np.dot(input,l1w))))
    #return np.multiply(input,np.dot(sigprime(np.dot(layer1,l2w)).T,np.dot(sigprime(np.dot(input,l1w)),l2w)))
    #return np.multiply(np.dot(np.dot(input.T,sigprime(np.dot(layer1,l2w))),l2w).T,sigprime(np.dot(input,l1w)).T).T
    return np.multiply(np.dot(np.dot(input.T,sigprime(np.dot(layer1,l2w))),l2w.T).T,sigprime(np.dot(input,l1w)).T).T
ffgrad=jacobian(feedforward)
print("jacobian")
print(ffgrad(np.array([[0.5]])))
print("d1")
print(dw1())
print("d2")
print(dw2())
