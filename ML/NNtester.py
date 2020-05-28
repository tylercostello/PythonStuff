from FinalSigSoftScratchNN import NN
import numpy as np
testInput=np.array([[0.9]])
wrt=0
print("input")
print(testInput)
newNN=NN(1,50,100)
print("output")
print(newNN.feedforward(testInput))

for x in range(1000):
    newNN.addw1(newNN.dw1(wrt))
    newNN.addw2(newNN.dw2(wrt))
    newNN.feedforward(testInput)

print("output")
print(newNN.feedforward(testInput))
print("d1")
print(newNN.dw1(wrt))
print("d2")
print(newNN.dw2(wrt))
