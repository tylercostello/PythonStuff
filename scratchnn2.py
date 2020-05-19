import numpy as np

def sig(x):
    return 1/(1+np.exp(-x))

def sigprime(x):
    return sig(x)*(1-sig(x))

hiddenneurons=2
outputneurons=3
input=np.random.rand(1,1)
l1w=np.random.rand(1,hiddenneurons)
l2w=np.random.rand(hiddenneurons,outputneurons)
layer1=sig(np.dot(input,l1w))

def feedforward(x):
    input[0,0]=x
    layer1=sig(np.dot(input,l1w))
    return sig(np.dot(sig(np.dot(input,l1w)),l2w))
print(feedforward(1))

def dw2():
    return np.dot(sigprime(np.dot(layer1,l2w)).T,layer1).T
def dw1():
    return np.multiply(input,np.multiply(np.dot(sigprime(np.dot(layer1,l2w)),l2w.T),sigprime(np.dot(input,l1w))))
print(dw1())
print(dw2())
