
import numpy as np
import matplotlib.pyplot as plt

#time
t = np.arange(0.0, 14.0, 0.01)

xt=2*t
yt=np.sin(t)

vx=[2]*1400
vx=np.asarray(vx)
vy=np.cos(t)

vf=np.sqrt((vx*vx+vy*vy))

theta=np.arctan(0.5*np.cos(0.5*t))

vfnoisy=vx+np.random.normal(0, 0.1, vx.shape)

thetanoisy=theta+np.random.normal(0, 0.1, theta.shape)
#np.var returns added noise squared
print(np.var(vfnoisy))
"""
plt.plot(t,vfnoisy)

plt.plot(t,thetanoisy)
#y(x)=sin(x/2)
"""
plt.plot(t,xt)
plt.plot(t,yt)
plt.plot(t,vx)
plt.plot(t,vy)
plt.plot(t,vf)
plt.plot(t,theta)

plt.show()
