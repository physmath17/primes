import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

p = np.zeros(1000)

for i in range(1000):
    p[i] = sp.prime(i+1)

plt.axes(projection='polar')
plt.scatter(p, p, s=1)
plt.show()
