import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

np.random.seed(1)
# setup
t = np.arange(0.0, 14.0, 0.01)

x = 0
y = 0
theta = np.pi / 2
b = 10
dt = 0.01
xTruth = [x]
yTruth = [y]
thetaTruth = [theta]

# vlTruth=20*(np.sin(t)+10)-100
vrTruth = 20 * (np.sin(t) + 10) - 100
# vlTruth=100*t
# vrTruth=100*t
# vrTruth=200*t
vlTruth = [110] * 1400
#vrTruth=[110]*1400
vl = vlTruth[0]
vr = vrTruth[0]

for counter in range(1, 1400):
    if vl == vr:
        x = x + vl * np.cos(theta) * dt
        y = y + vl * np.sin(theta) * dt
        theta = theta
        xTruth.append(x)
        yTruth.append(y)
        thetaTruth.append(theta)
        vl = vlTruth[counter]
        vr = vrTruth[counter]


    else:
        w = (vr - vl) / b
        r = (b / 2) * (vl + vr) / (vr - vl)

        x = r * np.sin(theta) * np.cos(w * dt) + r * np.cos(theta) * np.sin(w * dt) + x - r * np.sin(theta)
        y = r * np.sin(theta) * np.sin(w * dt) - r * np.cos(theta) * np.cos(w * dt) + y + r * np.cos(theta)
        theta = theta + w * dt
        # theta=theta%(2*np.pi)
        xTruth.append(x)
        yTruth.append(y)
        thetaTruth.append(theta)
        vl = vlTruth[counter]
        vr = vrTruth[counter]

vlTruth = np.asarray(vlTruth)
vlNoisy = vlTruth + np.random.normal(0, 0.5, vlTruth.shape)
vrTruth = np.asarray(vrTruth)
vrNoisy = vrTruth + np.random.normal(0, 0.5, vrTruth.shape)
thetaTruth = np.asarray(thetaTruth)
thetaNoisy = thetaTruth + np.random.normal(0, 0.5, thetaTruth.shape)
# plt.plot(xTruth,yTruth)
# plt.show()


prv_time = 0

x = np.array([
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

A = np.zeros((5, 5))
alvariance = 100
arvariance = 100


def aFunction(xInput, b, dt):
    xOutput = np.array([
        [0],
        [0],
        [0],
        [0],
        [0]
    ], dtype='float')

    x = xInput[0]
    y = xInput[1]
    theta = xInput[2]
    vl = xInput[3]
    vr = xInput[4]
    if vr == vl:
        x = x + vl * np.cos(theta) * dt
        y = y + vl * np.sin(theta) * dt
        theta = theta
    else:
        w = (vr - vl) / b
        r = (b / 2) * (vl + vr) / (vr - vl)

        x = r * np.sin(theta) * np.cos(w * dt) + r * np.cos(theta) * np.sin(w * dt) + x - r * np.sin(theta)
        y = r * np.sin(theta) * np.sin(w * dt) - r * np.cos(theta) * np.cos(w * dt) + y + r * np.cos(theta)
        theta = theta + w * dt

    xOutput[0] = x
    xOutput[1] = y
    xOutput[2] = theta
    xOutput[3] = vl
    xOutput[4] = vr
    return xOutput


dt_2 = dt * dt
dt_3 = dt * dt_2
dt_4 = dt * dt_3


def predict():
    global x, P, Q

    Q = np.zeros([5, 5])
    Q[0][0] = 0
    Q[0][1] = 0
    Q[0][2] = 0
    Q[0][3] = 0
    Q[0][4] = 0

    Q[1][0] = 0
    Q[1][1] = 0
    Q[1][2] = 0
    Q[1][3] = 0
    Q[1][4] = 0

    Q[2][0] = 0
    Q[2][1] = 0
    Q[2][2] = (dt_4 * alvariance + dt_4 * arvariance) / (4 * b * b)
    Q[2][3] = (-dt_3 * alvariance) / (2 * b)
    Q[2][4] = (dt_3 * arvariance) / (2 * b)

    Q[3][0] = 0
    Q[3][1] = 0
    Q[3][2] = (-dt_3 * alvariance) / (2 * b)
    Q[3][3] = dt_2 * alvariance
    Q[3][4] = 0

    Q[4][0] = 0
    Q[4][1] = 0
    Q[4][2] = (dt_3 * arvariance) / (2 * b)
    Q[4][3] = 0
    Q[4][4] = dt_2 * arvariance

    A = np.zeros((5, 5))

    if x[3] == x[4]:
        A[0][0] = 1
        A[0][1] = 0
        A[0][2] = -x[3] * dt * np.sin(x[2])
        A[0][3] = dt * np.cos(x[2])
        A[0][4] = 0

        A[1][0] = 0
        A[1][1] = 1
        A[1][2] = dt * x[3] * np.cos(x[2])
        A[1][3] = dt * np.sin(x[2])
        A[1][4] = 0

        A[2][0] = 0
        A[2][1] = 0
        A[2][2] = 1
        A[2][3] = 0
        A[2][4] = 0

        A[3][0] = 0
        A[3][1] = 0
        A[3][2] = 0
        A[3][3] = 1
        A[3][4] = 0

        A[4][0] = 0
        A[4][1] = 0
        A[4][2] = 0
        A[4][3] = 0
        A[4][4] = 1
    else:
        A[0][0] = 1
        A[0][1] = 0
        A[0][2] = (b * (x[4] + x[3]) * (np.cos(x[2] + dt * (x[4] - x[3]) / b) - np.cos(x[2]))) / (2 * (x[4] - x[3]))
        A[0][3] = (-x[4] * x[4] * dt * np.cos(x[2] + dt * (x[4] - x[3]) / b) + 2 * b * x[4] * np.sin(x[2] + dt * (x[4] - x[3]) / b) - 2 * b * x[4] * np.sin(x[2]) + x[3] * x[3] * dt * np.cos(x[2] + dt * (x[4] - x[3]) / b)) / (2 * (x[4] - x[3]) * (x[4] - x[3]))
        A[0][4] = (2 * x[3] * b * np.sin(x[2]) - 2 * x[3] * b * np.sin(x[2] + dt * (x[4] - x[3]) / b) + x[4] * x[4] * dt * np.cos(x[2] + dt * (x[4] - x[3]) / b) - x[3] * x[3] * dt * np.cos(x[2] + dt * (x[4] - x[3]) / b)) / (2 * (x[4] - x[3]) * (x[4] - x[3]))

        A[1][0] = 0
        A[1][1] = 1
        A[1][2] = (b * (x[4] + x[3]) * (np.sin(x[2] + dt * (x[4] - x[3]) / b) - np.sin(x[2]))) / (2 * (x[4] - x[3]))
        A[1][3] = (x[3] * x[3] * dt * np.cos(dt * (x[4] - x[3]) / b) * np.sin(x[2]) + x[3] * x[3] * dt * np.sin(dt * (x[4] - x[3]) / b) * np.cos(x[2]) + 2 * b * x[4] * np.sin(dt * (x[4] - x[3]) / b) * np.sin(x[2]) + 2 * b * x[4] * np.cos(x[2]) - x[4] * x[4] * dt * np.cos(dt * (x[4] - x[3]) / b) * np.sin(x[2]) - x[4] * x[4] * dt * np.sin(dt * (x[4] - x[3]) / b) * np.cos(x[2]) - 2 * b * x[4] * np.cos(dt * (x[4] - x[3]) / b) * np.cos(x[2])) / (2 * (x[4] - x[3]) * (x[4] - x[3]))
        A[1][4] = (x[4] * x[4] * dt * np.cos(dt * (x[4] - x[3]) / b) * np.sin(x[2]) + x[4] * x[4] * dt * np.sin(dt * (x[4] - x[3]) / b) * np.cos(x[2]) + 2 * b * x[3] * np.cos(dt * (x[4] - x[3]) / b) * np.cos(x[2]) - x[3] * x[3] * dt * np.cos(dt * (x[4] - x[3]) / b) * np.sin(x[2]) - 2 * b * x[3] * np.sin(dt * (x[4] - x[3]) / b) * np.sin(x[2]) - x[3] * x[3] * dt * np.sin(dt * (x[4] - x[3]) / b) * np.cos(x[2]) - 2 * b * x[3] * np.cos(x[2])) / (2 * (x[4] - x[3]) * (x[4] - x[3]))

        A[2][0] = 0
        A[2][1] = 0
        A[2][2] = 1
        A[2][3] = -dt / b
        A[2][4] = dt / b

        A[3][0] = 0
        A[3][1] = 0
        A[3][2] = 0
        A[3][3] = 1
        A[3][4] = 0

        A[4][0] = 0
        A[4][1] = 0
        A[4][2] = 0
        A[4][3] = 0
        A[4][4] = 1

    x = aFunction(x, b, dt)

    At = np.transpose(A)
    P = np.add(np.matmul(A, np.matmul(P, At)), Q)


def update(z):
    global x, P
    Y = np.subtract(z, np.matmul(H, x))
    Ht = np.transpose(H)
    S = np.add(np.matmul(H, np.matmul(P, Ht)), R)
    K = np.matmul(P, Ht)
    Si = inv(S)
    K = np.matmul(K, Si)
    x = np.add(x, np.matmul(K, Y))
    P = np.matmul(np.subtract(I, np.matmul(K, H)), P)


xList = []
xList.append(xTruth[0])
yList = []
yList.append(yTruth[0])
thetaList = []
thetaList.append(thetaTruth[0])
vlList = []
vlList.append(vlTruth[0])
vrList = []
vrList.append(vrTruth[0])
for counter in range(1, 1400):
    xList.append(x[0])
    yList.append(x[1])
    thetaList.append(x[2])
    vlList.append(x[3])
    vrList.append(x[4])
    z_sensors[0][0] = thetaNoisy[counter]
    z_sensors[1][0] = vlNoisy[counter]
    z_sensors[2][0] = vrNoisy[counter]
    predict()
    update(z_sensors)

plt.plot(xList, yList, label='truth')
plt.plot(xTruth, yTruth, label='estimated')
plt.legend()

"""
#plt.plot(t,vlNoisy)
plt.plot(t,vlTruth)
plt.plot(t,vlList)
#plt.plot(t,vrNoisy)
plt.plot(t,vrTruth)
plt.plot(t,vrList)
"""
"""
plt.plot(t,thetaTruth)
plt.plot(t,thetaList)
"""
plt.show()
