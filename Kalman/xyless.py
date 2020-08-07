import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

#setup
t = np.arange(0.0, 14.0, 0.01)
vl=89
vr=90
x=0
y=0
theta=np.pi/2
b=10
dt=0.01
xTruth=[x]
yTruth=[y]
thetaTruth=[theta]

vlTruth=[vl]*1400
#vlTruth=20*(np.sin(t)+1)
#print(vlTruth[0])
vrTruth=[vr]*1400

for counter in range(1,1400):
    if vl==vr:
        x=x+vl*np.cos(theta)
        y=y+vl*np.sin(theta)
        theta=theta
        xTruth.append(x)
        yTruth.append(y)
        thetaTruth.append(theta)
        print("here")
    else:
        w=(vr-vl)/b
        r=(b/2)*(vl+vr)/(vr-vl)

        x=r*np.sin(theta)*np.cos(w*dt)+r*np.cos(theta)*np.sin(w*dt)+x-r*np.sin(theta)
        y=r*np.sin(theta)*np.sin(w*dt)-r*np.cos(theta)*np.cos(w*dt)+y+r*np.cos(theta)
        theta=theta+w*dt
        #theta=theta%(2*np.pi)
        xTruth.append(x)
        yTruth.append(y)
        thetaTruth.append(theta)

vlTruth=np.asarray(vlTruth)
vlNoisy=vlTruth+np.random.normal(0, 0.5, vlTruth.shape)
vrTruth=np.asarray(vrTruth)
vrNoisy=vrTruth+np.random.normal(0, 0.5, vrTruth.shape)
thetaTruth=np.asarray(thetaTruth)
thetaNoisy=thetaTruth+np.random.normal(0, 0.5, thetaTruth.shape)
#plt.plot(xTruth,yTruth)
#plt.show()


prv_time = 0

x=np.array([
            [thetaTruth[0]],
            [vlTruth[0]],
            [vrTruth[0]]
            ], dtype='float')
#print(x)

P = np.array([
        [0.01, 0, 0],
        [0, 0.01, 0],
        [0, 0, 0.01],

        ])
H = np.identity(3)
I = np.identity(3)
z_sensors = np.zeros([3, 1])
Q = np.zeros([3, 3])
R = np.array([
        [0.25, 0, 0],
        [0, 0.25, 0],
        [0, 0, 0.25]
        ])

A = np.zeros((3,3))

def aFunction(xInput,b,dt):
    xOutput=np.array([
                [0],
                [0],
                [0]
                ], dtype='float')

    theta=xInput[0]
    vl=xInput[1]
    vr=xInput[2]
    if vr==vl:
        theta=theta
        print("here")
    else:
        w=(vr-vl)/b
        theta=theta+w*dt

    xOutput[0]=theta
    xOutput[1]=vl
    xOutput[2]=vr
    return xOutput

def predict():
    global x, P, Q

    """needs to be jacobian"""
    A = np.zeros((3,3))

    if x[1]==x[2]:
        #do otherjacobian
        print("here")
    else:
        #jacobian

        A[0][0]=1
        A[0][1]=-dt/b
        A[0][2]=dt/b

        A[1][0]=0
        A[1][1]=1
        A[1][2]=0

        A[2][0]=0
        A[2][1]=0
        A[2][2]=1


    x = aFunction(x, b, dt)

    At = np.transpose(A)
    P = np.add(np.matmul(A, np.matmul(P, At)), Q)
def update(z):
    global x, P
    Y = np.subtract(z_sensors, np.matmul(H, x))
    Ht = np.transpose(H)
    S = np.add(np.matmul(H, np.matmul(P, Ht)), R)
    K = np.matmul(P, Ht)
    Si = inv(S)
    K = np.matmul(K, Si)
    x = np.add(x, np.matmul(K, Y))
    P = np.matmul(np.subtract(I ,np.matmul(K, H)), P)
def calcXY(x,y,theta,vl,vr,b,dt):
    if vr==vl:
        x=x+vl*np.cos(theta)
        y=y+vl*np.sin(theta)
        print("here")
    else:
        w=(vr-vl)/b
        r=(b/2)*(vl+vr)/(vr-vl)

        x=r*np.sin(theta)*np.cos(w*dt)+r*np.cos(theta)*np.sin(w*dt)+x-r*np.sin(theta)
        y=r*np.sin(theta)*np.sin(w*dt)-r*np.cos(theta)*np.cos(w*dt)+y+r*np.cos(theta)
    return np.array([x,y])
xList=[]
xList.append(xTruth[0])
yList=[]
yList.append(yTruth[0])
thetaList=[]
thetaList.append(thetaTruth[0])
vlList=[]
vlList.append(vlTruth[0])
#print(vlList)
vrList=[]
vrList.append(vrTruth[0])
prevX=xList[0]
prevY=yList[0]
for counter in range(1,1400):
    #print(x[3])
    thetaList.append(x[0])
    vlList.append(x[1])
    vrList.append(x[2])
    z_sensors[0][0]=thetaNoisy[counter]
    z_sensors[1][0]=vlNoisy[counter]
    z_sensors[2][0]=vrNoisy[counter]
    predict()
    #print(x)
    update(z_sensors)
    xyArray=calcXY(prevX,prevY,x[0],x[1],x[2],b,dt)
    xList.append(xyArray[0])
    yList.append(xyArray[1])
    prevX=xyArray[0]
    prevY=xyArray[1]
    #print(x)
plt.plot(xList,yList)
plt.plot(xTruth,yTruth)

#plt.plot(t,vlNoisy)
#plt.plot(t,vlTruth)
#plt.plot(t,vlList)
#plt.plot(t,vrNoisy)
#plt.plot(t,vrTruth)
#plt.plot(t,vrList)
#plt.plot(t,thetaTruth)
#plt.plot(t,thetaList)
plt.show()
