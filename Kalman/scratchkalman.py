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

x=0
a=1
p=1
q=0.05
y=0
z=0
h=1
k=0
i=1
r=0.5
for counter in range(200):
    x=a*x
    p=a*p*a+q
    z=s[counter]
    y=z-h*x
    k=(p*h)/((h*p*h)+r)
    x=x+k*y
    p=(i-k*h)*p
    pointsList.append(x)




#plotting
fig, ax = plt.subplots()
ax.plot(t, s)
ax.plot(t, v)

ax.plot(t,pointsList,color='red')
ax.grid()
plt.show()
