#implements algorithm from http://www.cs.columbia.edu/~allen/F15/NOTES/icckinematics.pdf
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

t = np.arange(0.0, 14.0, 0.01)

#from what I understand this is the wheel's forward velocity, so it is radius * angular velocity
#Left Wheel Speed
vl=50
#Right Wheel Speed
vr=25
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
thetaList=[theta]


for counter in range(1,1400):


    if vl==vr:
        x=x+vl*np.cos(theta)*dt
        y=y+vl*np.sin(theta)*dt
        theta=theta
        xList.append(x)
        yList.append(y)
        thetaList.append(theta)
    else:
        w=(vr-vl)/b
        r=(b/2)*(vl+vr)/(vr-vl)
        #print(r)
        x=r*np.sin(theta)*np.cos(w*dt)+r*np.cos(theta)*np.sin(w*dt)+x-r*np.sin(theta)
        y=r*np.sin(theta)*np.sin(w*dt)-r*np.cos(theta)*np.cos(w*dt)+y+r*np.cos(theta)
        theta=theta+w*dt
        theta=theta%(2*np.pi)
        xList.append(x)
        yList.append(y)
        thetaList.append(theta)

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.plot(xList,yList)
#plt.plot(t,yList)
#plt.plot(t,thetaList)
plt.show()
