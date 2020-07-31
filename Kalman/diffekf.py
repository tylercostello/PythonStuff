import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
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
x=np.array([
            [0],
            [0],
            [0],
            [0],
            [0]
            ], dtype='float')
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
P = np.array([
        [0.01, 0, 0, 0],
        [0, 0.01, 0, 0],
        [0, 0, 0.01, 0],
        [0, 0, 0, 0.01]
        ])

H = np.array([
        [0, 0, 1.0, 0, 0],
        [0, 0, 0, 1.0, 0],
        [0, 0, 0, 0, 1.0]
        ])
I = np.identity(5)
z_sensors = np.zeros([3, 1])
R = np.array([
        [0.25, 0, 0],
        [0, 0.25, 0]
        [0, 0, 0.25]
        ])
Q = np.zeros([5, 5])


def predict():
    # Predict Step
    global x, P, Q
    #predicted sensor values
    #X = A * X
    x = aFunction(x, 1, 0.01)

    aJacobian = np.array([
    []
    ])

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
