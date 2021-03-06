
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt


#Ground Truth
np.random.seed(1)
t = np.arange(0.0, 140.00, 0.01)

xt=2*t
#yt=3*t
yt=np.sin(t)

vx=[2]*14000
vx=np.asarray(vx)
#vy=[3]*14000
#vy=np.asarray(vy)
vy=np.cos(t)

#What the sensor readings will be from encoders
xtnoisy=xt+np.random.normal(0, 0.5, xt.shape)
ytnoisy=yt+np.random.normal(0, 0.5, yt.shape)


prv_time = 0

#Initialzing x with first sensor readings
x = np.array([
        [xtnoisy[0]],
        [ytnoisy[0]],
        [0],
        [0]
        ])

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


#Initialize matrices P and A

#equation variances
#Doesn't really matter the kalman filter will figure it out
P = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1000, 0],
        [0, 0, 0, 1000]
        ])
#equation creator
"""
Px(t+1) = Px + delta_t * vx
Py(t+1) = Py + delta_t * vy
Vx(t+1) = Vx
Vy(t+1) = Vy
"""
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
z_encoder = np.zeros([2, 1])
#sensor variances
R = np.array([
        [0.25, 0],
        [0, 0.25]
        ])
#A guess on how random our acceleration will be
noise_ax = 5
noise_ay = 5
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
    #X = A * X
    x = np.matmul(A, x)

    At = np.transpose(A)

    #predicted value variances
    #P = A * P * AT + Q
    P = np.add(np.matmul(A, np.matmul(P, At)), Q)
    #P = np.matmul(A, np.matmul(P, At))

def update(z):
    global x, P
    #Difference between predicted and measured sensor readings
    #Y = Z — H * X
    Y = np.subtract(z_encoder, np.matmul(H, x))

    Ht = np.transpose(H)

    #Kalman gain
    #( P * HT ) / ( ( H * P * HT ) + R )
    S = np.add(np.matmul(H, np.matmul(P, Ht)), R)
    K = np.matmul(P, Ht)
    Si = inv(S)
    K = np.matmul(K, Si)

    #final predicted values
    #X = X + K * Y
    x = np.add(x, np.matmul(K, Y))

    #final variances
    #P = ( I — K * H ) * P
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
    z_encoder[0][0]=xtnoisy[i]
    z_encoder[1][0]=ytnoisy[i]

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

    #Collecting ground truths
    #Call Kalman Filter Predict and Update functions.
    predict()
    update(z_encoder)
    sensorList.append(z_encoder[0][0])
    xList.append(x[0])
    yList.append(x[1])
    vxList.append(x[2])
    vyList.append(x[3])

"""
plt.plot(t,xtnoisy)
plt.plot(t,xList)
plt.plot(t,xt)
"""


plt.plot(t,ytnoisy)
plt.plot(t,yt)
plt.plot(t,yList)


"""
plt.plot(t,vx)
plt.plot(t,vxList)
"""

"""
plt.plot(t,vy)
plt.plot(t,vyList)
"""

plt.show()
