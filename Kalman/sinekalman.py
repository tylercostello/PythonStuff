#algorithm credit to https://www.youtube.com/watch?v=biY7F-tLwE8

import numpy as np
import matplotlib.pyplot as plt

#time
t = np.arange(0.0, 2.0, 0.01)
#true function
v=np.sin(2 * np.pi * t)
#sensor input
s = np.sin(2 * np.pi * t)
np.random.seed(1)
s=s+np.random.normal(0, 0.2, s.shape)
#print(np.var(s))



pointsList=[]
r=0.5057002776436168 # sensor covariance, done by np.var(s)
q=0.05
pc=0
k=0
p=1
xp=0
zp=0
xe=0
for counter in range(200):
    #predict next covariance
    pc=p+q
    #compute kalman gain
    k=pc/(pc+r)
    #update covariance
    p=(1-k)*pc
    #update state
    xp=xe
    zp=xp
    xe=k*(s[counter]-zp)+xp
    pointsList.append(xe)

#calculates average distance between true function and kalman filter
sav=0
for newCounter in range(200):
    sav=sav+(pointsList[newCounter]-v[newCounter])
sav=sav/200
print(sav)
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
ma=moving_average(s,n=5)
for x in range(4):
    ma=np.insert(ma,0,s[x])
#plotting
fig, ax = plt.subplots()
#ax.plot(t, s)
ax.plot(t, v)
ax.plot(t, ma,color='yellow')
ax.plot(t,pointsList,color='red')
ax.grid()
plt.show()
