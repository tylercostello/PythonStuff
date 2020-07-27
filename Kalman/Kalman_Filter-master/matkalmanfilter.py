
import numpy as np
import pandas as pd
from numpy.linalg import inv
import matplotlib.pyplot as plt



#np.random.seed(1)
t = np.arange(0.0, 140.00, 0.01)

xt=2*t
yt=3*t
#yt=3*t

vx=[2]*14000
vx=np.asarray(vx)
vy=[3]*14000
#vy=np.asarray(vy)
#vy=np.cos(t)

#vf=np.sqrt((vx*vx+vy*vy))
#theta=[np.arctan(3/2)]*1400
#theta=np.asarray(theta)
#theta=np.arctan(0.5*np.cos(0.5*xt))

xtnoisy=xt+np.random.normal(0, 0.5, xt.shape)

ytnoisy=yt+np.random.normal(0, 0.5, yt.shape)
#vfnoisy=vf+np.random.normal(0, 0.5, vf.shape)
#vfnoisy=vf
#thetanoisy=theta
#thetanoisy=theta+np.random.normal(0, 0.5, theta.shape)





prv_time = 0

x = np.array([
        [xt[0]],
        [yt[0]],
        [vx[0]],
        [vy[0]]
        ])


#Initialize matrices P and A

#equation variances
P = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
        ])
#equation creator
A = np.array([
        [1.0, 0, 1.0, 0],
        [0, 1.0, 0, 1.0],
        [0, 0, 1.0, 0],
        [0, 0, 0, 1.0]
        ])
#shaper
H = np.array([
        [1.0, 0, 0, 0],
        [0, 1.0, 0, 0]
        ])
I = np.identity(4)
z_lidar = np.zeros([2, 1])
#sensor variances
R = np.array([
        [0.25, 0],
        [0, 0.25]
        ])
noise_ax = 1
noise_ay = 1
Q = np.zeros([4, 4])

def predict():
    # Predict Step
    global x, P, Q
    x = np.matmul(A, x)
    #predicted sensor values
    At = np.transpose(A)
    #predicted value variances
    P = np.add(np.matmul(A, np.matmul(P, At)), Q)
    #P = np.matmul(A, np.matmul(P, At))

def update(z):
    global x, P
    # Measurement update step
    Y = np.subtract(z_lidar, np.matmul(H, x))
    Ht = np.transpose(H)
    S = np.add(np.matmul(H, np.matmul(P, Ht)), R)
    K = np.matmul(P, Ht)
    Si = inv(S)
    K = np.matmul(K, Si)

    # New state
    #final predicted values
    x = np.add(x, np.matmul(K, Y))
    #final variances
    P = np.matmul(np.subtract(I ,np.matmul(K, H)), P)



#**********************Iterate through main loop********************
#Begin iterating through sensor data
xList=[]
xList.append(xt[0])
yList=[]
yList.append(yt[0])
vxList=[]
vxList.append(vx[0])
vyList=[]
vyList.append(vy[0])

sensorList=[]
groundList=[]
tList=[]
for i in range (1,14000):
    new_measurement = np.zeros((2,1))
    #print(new_measurement)
    new_measurement[0][0]=xtnoisy[i]
    new_measurement[1][0]=ytnoisy[i]

    #Calculate Timestamp and its power variables
    cur_time = i/100
    tList.append(cur_time)
    dt = cur_time - prv_time
    prv_time = cur_time
    dt_2 = dt * dt
    dt_3 = dt_2 * dt
    dt_4 = dt_3 * dt
    #Updating matrix A with dt value
    A[0][2] = dt
    A[1][3] = dt
    #Updating Q matrix
    Q[0][0] = dt_4/4*noise_ax
    Q[0][2] = dt_3/2*noise_ax
    Q[1][1] = dt_4/4*noise_ay
    Q[1][3] = dt_3/2*noise_ay
    Q[2][0] = dt_3/2*noise_ax
    Q[2][2] = dt_2*noise_ax
    Q[3][1] = dt_3/2*noise_ay
    Q[3][3] = dt_2*noise_ay
    #Updating sensor readings
    z_lidar[0][0] = new_measurement[0][0]
    z_lidar[1][0] = new_measurement[1][0]
    #Collecting ground truths
    #Call Kalman Filter Predict and Update functions.
    predict()
    update(z_lidar)
    sensorList.append(z_lidar[0][0])
    xList.append(x[0])
    yList.append(x[1])
    vxList.append(x[2])
    vyList.append(x[3])



    #print('iteration', i, 'x: ', x)
#plt.plot(t,xList)
#plt.plot(t,xt)

#plt.plot(t,ytnoisy)
#plt.plot(t,yt)
#plt.plot(t,yList)

plt.plot(t,vxList)
plt.plot(t,vx)

#plt.plot(t,vfnoisy*np.sin(thetanoisy))
#plt.plot(t,vyList)
#plt.plot(t,vy)
#plt.plot(xt,yt)
#plt.plot(xList,yList)

#plt.plot(t,theta)

#plt.plot(t,vf)
plt.show()
