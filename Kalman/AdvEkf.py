import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

#setup
t = np.arange(0.0, 14.0, 0.01)
vl=50
vr=25
x=0
y=0
theta=np.pi/2
b=1
dt=0.01
xTruth=[x]
yTruth=[y]
thetaTruth=[theta]

vlTruth=[vl]*1400

vrTruth=[vr]*1400

for counter in range(1,1400):
    if vl==vr:
        x=x+vl*np.cos(theta)
        y=y+vl*np.sin(theta)
        theta=theta
        xTruth.append(x)
        yTruth.append(y)
        thetaTruth.append(theta)
    else:
        w=(vr-vl)/b
        r=(b/2)*(vl+vr)/(vr-vl)

        x=r*np.sin(theta)*np.cos(w*dt)+r*np.cos(theta)*np.sin(w*dt)+x-r*np.sin(theta)
        y=r*np.sin(theta)*np.sin(w*dt)-r*np.cos(theta)*np.cos(w*dt)+y+r*np.cos(theta)
        theta=theta+w*dt
        theta=theta%(2*np.pi)
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
            [xTruth[0]],
            [yTruth[0]],
            [thetaTruth[0]],
            [vlTruth[0]],
            [vrTruth[0]]
            ], dtype='float')


P = np.array([
        [0.01, 0, 0, 0, 0],
        [0, 0.01, 0, 0, 0],
        [0, 0, 0.01, 0, 0],
        [0, 0, 0, 0.01, 0],
        [0, 0, 0, 0, 0.01]
        ])
H = np.array([
        [0, 0, 1.0, 0, 0],
        [0, 0, 0, 1.0, 0],
        [0, 0, 0, 0, 1.0]
        ])
I = np.identity(5)
z_sensors = np.zeros([3, 1])
Q = np.zeros([5, 5])
R = np.array([
        [0.25, 0, 0],
        [0, 0.25, 0],
        [0, 0, 0.25]
        ])

A = np.ones((5,5))

def aFunction(xInput,b,dt):
    xOutput=np.array([
                [0],
                [0],
                [0],
                [0],
                [0]
                ], dtype='float')

    x=xInput[0]
    y=xInput[1]
    theta=xInput[2]
    vl=xInput[3]
    vr=xInput[4]
    if vr==vl:
        x=x+vl*np.cos(theta)
        y=y+vl*np.sin(theta)
        theta=theta
    else:
        w=(vr-vl)/b
        r=(b/2)*(vl+vr)/(vr-vl)

        x=r*np.sin(theta)*np.cos(w*dt)+r*np.cos(theta)*np.sin(w*dt)+x-r*np.sin(theta)
        y=r*np.sin(theta)*np.sin(w*dt)-r*np.cos(theta)*np.cos(w*dt)+y+r*np.cos(theta)
        theta=theta+w*dt

    xOutput[0]=x
    xOutput[1]=y
    xOutput[2]=theta
    xOutput[3]=vl
    xOutput[4]=vr
    return xOutput

def predict():
    global x, P, Q
    x = aFunction(x, 1, 0.01)

    """needs to be jacobian"""
    A = np.ones((5,5))

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
xList=[]
xList.append(xTruth[0])
yList=[]
yList.append(xTruth[1])
thetaList=[]
thetaList.append(xTruth[2])
vlList=[]
vlList.append(xTruth[3])
vrList=[]
vrList.append(xTruth[4])
for counter in range(1,1400):
    z_sensors[0][0]=thetaNoisy[counter]
    z_sensors[1][0]=vlNoisy[counter]
    z_sensors[2][0]=vrNoisy[counter]
    predict()
    update(z_sensors)
    xList.append(x[0])
    yList.append(x[1])
    thetaList.append(x[2])
    vlList.append(x[3])
    vrList.append(x[4])
plt.plot(xList,yList)
plt.show()
