import numpy as np

def sig(x):
    return 1/(1+np.exp(-x))
def sigprime(x):
    return sig(x)*(1-sig(x))
def soft(x):
    return np.exp(x)/np.sum(np.exp(x))
def softprime(x):
    return soft(x)*(1-soft(x))
myinput=1
inputneurons=1
hiddenneurons=2
outputneurons=4

input=np.random.uniform(-1,1,(1,inputneurons))
l1w=np.random.uniform(-1,1,(inputneurons,hiddenneurons))
l2w=np.random.uniform(-1,1,(hiddenneurons,outputneurons))

layer1=sig(np.dot(input,l1w))
print("input")
print(myinput)
print("weights1")
print(l1w)
print("weights2")
print(l2w)
def feedforward(x):
    input[0,0]=x
    layer1=sig(np.dot(input,l1w))
    return soft(np.dot(sig(np.dot(input,l1w)),l2w))
print("output")
print(feedforward(myinput))

def dw2():
    return np.dot(softprime(np.dot(layer1,l2w)).T,layer1).T
def dw1():
    return np.multiply(np.dot(np.dot(input.T,softprime(np.dot(layer1,l2w))),l2w.T).T,sigprime(np.dot(input,l1w)).T).T

print("d1")
print(dw1())
print("d2")
print(dw2())
