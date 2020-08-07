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
vlNoisy=vlTruth+np.random.normal(0, 0.001, vlTruth.shape)
vrTruth=np.asarray(vrTruth)
vrNoisy=vrTruth+np.random.normal(0, 0.001, vrTruth.shape)
thetaTruth=np.asarray(thetaTruth)
thetaNoisy=thetaTruth+np.random.normal(0, 0.001, thetaTruth.shape)
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
        [5, 0, 0],
        [0, 5, 0],
        [0, 0, 5]
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
        print("here")
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

    """needs to be jacobian"""
    A = np.ones((5,5))

    if x[3]==x[4]:
        #do otherjacobian
        print("here")
    else:
        #jacobian
        A[0][0]=1
        A[0][1]=0
        A[0][2]=(b*(x[4]+x[3])*(np.cos(x[2]+dt*(x[4]-x[3])/b)-np.cos(x[2])))/(2*(x[4]-x[3]))
        A[0][3]=(-x[4]*x[4]*dt*np.cos(x[2]+dt*(x[4]-x[3])/b)+2*b*x[4]*np.sin(x[2]+dt*(x[4]-x[3])/b)-2*b*x[4]*np.sin(x[2])+x[3]*x[3]*dt*np.cos(x[2]+dt*(x[4]-x[3])/b))/(2*(x[4]-x[3])*(x[4]-x[3]))
        A[0][4]=(2*x[3]*b*np.sin(x[2])-2*x[3]*b*np.sin(x[2]+dt*(x[4]-x[3])/b)+x[4]*x[4]*dt*np.cos(x[2]+dt*(x[4]-x[3])/b)-x[3]*x[3]*dt*np.cos(x[2]+dt*(x[4]-x[3])/b))/(2*(x[4]-x[3])*(x[4]-x[3]))
        A[1][0]=0
        A[1][1]=1
        A[1][2]=(b*(x[4]+x[3])*(np.sin(x[2]+dt*(x[4]-x[3])/b)-np.sin(x[2])))/(2*(x[4]-x[3]))
        A[1][3]=(x[3]*x[3]*dt*np.cos(dt*(x[4]-x[3])/b)*np.sin(x[2])+x[3]*x[3]*dt*np.sin(dt*(x[4]-x[3])/b)*np.cos(x[2])+2*b*x[4]*np.sin(dt*(x[4]-x[3])/b)*np.sin(x[2])+2*b*x[4]*np.cos(x[2])-x[4]*x[4]*dt*np.cos(dt*(x[4]-x[3])/b)*np.sin(x[2])-x[4]*x[4]*dt*np.sin(dt*(x[4]-x[3])/b)*np.cos(x[2])-2*b*x[4]*np.cos(dt*(x[4]-x[3])/b)*np.cos(x[2]))/(2*(x[4]-x[3])*(x[4]-x[3]))
        A[1][4]=(x[4]*x[4]*dt*np.cos(dt*(x[4]-x[3])/b)*np.sin(x[2])+x[4]*x[4]*dt*np.sin(dt*(x[4]-x[3])/b)*np.cos(x[2])+2*b*x[3]*np.cos(dt*(x[4]-x[3])/b)*np.cos(x[2])-x[3]*x[3]*dt*np.cos(dt*(x[4]-x[3])/b)*np.sin(x[2])-2*b*x[3]*np.sin(dt*(x[4]-x[3])/b)*np.sin(x[2])-x[3]*x[3]*dt*np.sin(dt*(x[4]-x[3])/b)*np.cos(x[2])-2*b*x[3]*np.cos(x[2]))/(2*(x[4]-x[3])*(x[4]-x[3]))
        A[2][0]=0
        A[2][1]=0
        A[2][2]=1
        A[2][3]=-dt/b
        A[2][4]=dt/b
        A[3][0]=0
        A[3][1]=0
        A[3][2]=0
        A[3][3]=1
        A[3][4]=0
        A[4][0]=0
        A[4][1]=0
        A[4][2]=0
        A[4][3]=0
        A[4][4]=1


    x = aFunction(x, 1, 0.01)
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
plt.plot(t,vrNoisy)
plt.plot(t,vrList)
plt.show()
