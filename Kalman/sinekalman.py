import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
t = np.arange(0.0, 2.0, 0.01)
v=np.sin(2 * np.pi * t)
s = np.sin(2 * np.pi * t)
print(np.var(s))
s=s+np.random.normal(0, 0.2, s.shape)
print(np.var(s))


pointsList=[]
r=0.5057002776436168
q=0.05
pc=0
g=0
p=1
xp=0
zp=0
xe=0
for counter in range(200):
    pc=p+q
    g=pc/(pc+r)
    p=(1-g)*pc
    xp=xe
    zp=xp
    xe=g*(s[counter]-zp)+xp
    pointsList.append(xe)

fig, ax = plt.subplots()

ax.plot(t, s)
ax.plot(t, v)
ax.plot(t,pointsList)

ax.grid()

plt.show()
