import numpy as np

def sig(x):
    return 1/(1+np.exp(-x))

def sigprime(x):
    return sig(x)*(1-sig(x))

input=np.random.rand(1,1)
l1w=np.random.rand(1,2)
l2w=np.random.rand(2,1)
print("Input")
print(input)
print("L1W")
print(l1w)
print("L2W")
print(l2w)
def feedforward(x):
    return sig(np.dot(sig(np.dot(input,l1w)),l2w))
print("Output")
print(feedforward(input))

print("DY and DZ")
#dy and dz
print(np.dot(sigprime(np.dot(sig(np.dot(input,l1w)),l2w)),sig(np.dot(input,l1w))))

print("DW and DX")
#dw and dx
print(np.multiply(l2w,np.dot(sigprime(np.dot(sig(np.dot(input,l1w)),l2w)),np.dot(input,sigprime(np.dot(input,l1w)))).T))

print("Gradient")
yz=np.dot(sigprime(np.dot(sig(np.dot(input,l1w)),l2w)),sig(np.dot(input,l1w)))
flattenWX=np.multiply(l2w,np.dot(sigprime(np.dot(sig(np.dot(input,l1w)),l2w)),np.dot(input,sigprime(np.dot(input,l1w)))).T).T
combined=np.concatenate((flattenWX,yz),axis=1).T
print(combined)

print("Gradient of Log")
print(combined/feedforward(input))
