
import numpy as np
import matplotlib.pyplot as plt

#time
t = np.arange(0.0, 14.0, 0.01)
#true function
#original=3*t
original=np.sin(t)
#sensor input


noisy=original+np.random.normal(0, 0.1, original.shape)
#print(np.var(s))

theta=np.arctan(np.cos(t))
thetaNoise=theta+np.random.normal(0, 0.1, original.shape)

velocity=10
vy=velocity*np.sin(theta)
vx=velocity*np.cos(theta)
vcheck=vy*vy+vx*vx

#print(np.var(thetaNoise))
pointsList=[]

x=0
a=1
p=1
q=0.05
y=0
z=0
h=1
k=0
i=1
r=0.01
for counter in range(1400):

    x=a*x
    p=a*p*a+q
    z=noisy[counter]
    y=z-h*x
    k=(p*h)/((h*p*h)+r)
    x=x+k*y
    p=(i-k*h)*p
    pointsList.append(x)



#plotting
"""
fig, ax = plt.subplots()
ax.plot(t, s)
ax.plot(t, v)

ax.plot(t,pointsList,color='red')
ax.grid()
plt.show()
"""
#iy=np.cumsum(vy)


plt.plot(t,noisy)
plt.plot(t,pointsList)
plt.plot(t,original)
#plt.plot(t,theta)
#plt.plot(t,vy)
#print(vy)
#plt.plot(t,vx)
#plt.plot(t,iy2)
#print(iy)
#plt.plot(t,thetaNoise)
plt.show()
