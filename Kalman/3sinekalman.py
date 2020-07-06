#algorithm credit to https://www.youtube.com/watch?v=biY7F-tLwE8

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0.0, 2.0, 0.01)
v=np.sin(2 * np.pi * t)
s = np.sin(2 * np.pi * t)
s2 = np.sin(2 * np.pi * t)
s3 = np.sin(2 * np.pi * t)
#print(np.var(s))
np.random.seed(1)
s=s+np.random.normal(0, 0.2, s.shape)
np.random.seed(2)
s2=s2+np.random.normal(0, 0.2, s2.shape)
np.random.seed(3)
s3=s3+np.random.normal(0, 0.2, s3.shape)
#print(np.var(s))


pointsList=[]
r=0.5057002776436168
q=0.01
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
    #update state 3 times
    xp=xe
    zp=xp
    xe=k*(s[counter]-zp)+xp
    xp=xe
    zp=xp
    xe=k*(s2[counter]-zp)+xp
    xp=xe
    zp=xp
    xe=k*(s3[counter]-zp)+xp
    pointsList.append(xe)
sav=0

for newCounter in range(200):
    sav=sav+(pointsList[newCounter]-v[newCounter])
sav=sav/200
print(sav)
fig, ax = plt.subplots()

#ax.plot(t, s)
#ax.plot(t,s2)
ax.plot(t, v)
ax.plot(t,pointsList,color='red')

ax.grid()

plt.show()
