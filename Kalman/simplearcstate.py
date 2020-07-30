import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

t = np.arange(0.0, 14.0, 0.01)

sl=50
sr=0
x=0
y=0
theta=np.pi/2
b=1
wr=1
xList=[0]
yList=[0]
xList1=[0]
yList1=[0]
xList2=[0]
yList2=[0]

for counter in range(1399):


    x=wr*0.5*(sr+sl)*np.cos(theta)+x
    y=wr*0.5*(sr+sl)*np.sin(theta)+y
    theta=(wr/b)*(sr-sl)+theta
    xList.append(x)
    yList.append(y)



    x=((sl+sr)/2)*np.cos(theta)+x
    y=((sl+sr)/2)*np.sin(theta)+y
    theta=(sl-sr)/(2*b)+theta
    xList1.append(x)
    yList1.append(y)

    x=x-0.5*(sr+sl)*np.sin(theta)
    y=y+0.5*(sr+sl)*np.cos(theta)
    theta=theta+(sr-sl)
    xList2.append(x)
    yList2.append(y)


#lt.xlim(-500,500)
#plt.ylim(-500,500)
plt.plot(xList,yList)
plt.plot(xList1,yList1)
plt.plot(xList2,yList2)
plt.show()
