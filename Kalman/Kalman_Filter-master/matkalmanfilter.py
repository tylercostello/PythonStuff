
import numpy as np
import pandas as pd
from numpy.linalg import inv
import matplotlib.pyplot as plt

np.random.seed(1)
t = np.arange(0.0, 140.00, 0.01)

xt=2*t
yt=3*t
#yt=np.sin(t)

vx=[2]*14000
vx=np.asarray(vx)
vy=[3]*14000
vy=np.asarray(vy)
#vy=np.cos(t)


xtnoisy=xt+np.random.normal(0, 0.5, xt.shape)
ytnoisy=yt+np.random.normal(0, 0.5, yt.shape)


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
#Identity
I = np.identity(4)
#Where sensor readings will be stored
z_lidar = np.zeros([2, 1])
#sensor variances
R = np.array([
        [0.25, 0],
        [0, 0.25]
        ])
#A guess on how random our acceleration will be
noise_ax = 1
noise_ay = 1
Q = np.zeros([4, 4])

"""
A. Predict:
a. X = A * X
b. P = A * P * AT + Q
B. Update
a. Y = Z — H * X
b. K = ( P * HT ) / ( ( H * P * HT ) + R )
c. X = X + K * Y
d. P = ( I — K * H ) * P
"""

def predict():
    # Predict Step
    global x, P, Q
    #predicted sensor values
    x = np.matmul(A, x)

    At = np.transpose(A)
    #predicted value variances
    P = np.add(np.matmul(A, np.matmul(P, At)), Q)

def update(z):
    global x, P
    # Measurement update step
    #Difference between predicted and measured sensor readings
    Y = np.subtract(z_lidar, np.matmul(H, x))
    Ht = np.transpose(H)
    S = np.add(np.matmul(H, np.matmul(P, Ht)), R)
    K = np.matmul(P, Ht)
    Si = inv(S)
    #Kalman gain
    K = np.matmul(K, Si)

    #final predicted values
    x = np.add(x, np.matmul(K, Y))
    #final variances
    P = np.matmul(np.subtract(I ,np.matmul(K, H)), P)

#Main loop

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


plt.plot(t,xtnoisy)
plt.plot(t,xList)
plt.plot(t,xt)


"""
plt.plot(t,ytnoisy)
plt.plot(t,yt)
plt.plot(t,yList)
"""

"""
plt.plot(t,vx)
plt.plot(t,vxList)
"""

"""
plt.plot(t,vy)
plt.plot(t,vyList)
"""

plt.show()
