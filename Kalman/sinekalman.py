import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
t = np.arange(0.0, 2.0, 0.01)
v=1 + np.sin(2 * np.pi * t)
s = 1 + np.sin(2 * np.pi * t)
s=s+np.random.normal(0, 0.2, s.shape)
print(np.var(s))

fig, ax = plt.subplots()
ax.plot(t, s)
ax.plot(t, v)
ax.grid()

plt.show()
