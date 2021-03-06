#implements algorithm from http://www.cs.columbia.edu/~allen/F15/NOTES/icckinematics.pdf
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

t = np.arange(0.0, 14.0, 0.01)

#from what I understand this is the wheel's forward velocity, so it is radius * angular velocity
#Left Wheel Speed
sl=50
#Right Wheel Speed
sr=25
#Starting X
x=0
#Starting Y
y=0
#Starting Theta
theta=np.pi/2
#Robot Width
b=1
dt=0.01
xList=[x]
yList=[y]

m1=np.array([
            [x],
            [y],
            [theta]
            ],
            dtype='float')

for counter in range(1399):


    w=(sr-sl)/b
    r=(b/2)*(sl+sr)/(sr-sl)
    icc=np.array([
                [m1[0]-r*np.sin(m1[2])],
                [m1[1]+r*np.cos(m1[2])]
                ],
                dtype='float')
    m2=np.array([
                [np.cos(w*dt), -np.sin(w*dt),0],
                [np.sin(w*dt),np.cos(w*dt),0],
                [0,0,1]
                ],
                dtype='float')
    #print(m2.shape)
    m3=np.array([
                [m1[0]-icc[0]],
                [m1[1]-icc[1]],
                [m1[2]]
                ],
                dtype='float')

    m3.shape=(3,1)
    #print(m3.shape)
    m4=np.array([
                [icc[0]],
                [icc[1]],
                [w*dt]
                ],
                dtype='float')

    m1=np.add(np.matmul(m2,m3),m4)
    xList.append(m1[0])
    yList.append(m1[1])
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.plot(xList,yList)
#plt.plot(t,yList)
plt.show()
