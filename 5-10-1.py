from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(r,t):
    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + sin(t)**2
    return np.array([fx, fy])

t = np.linspace(0, 10, 1000)
x = np.ones_like(t)
y = np.ones_like(t)
k = np.zeros([4,2], float)   ## k1 (=c1) with matrix

h = t[1] - t[0]
for i in range(1, len(t)):
    r = [x[i-1], y[i-1]]
    k[0] = h * f(r,t[i-1])
    k[1] = h * f(r + k[0]/2, t[i-1] + h/2)
    k[2] = h * f(r + k[1]/2, t[i-1] + h/2)
    k[3] = h * f(r + k[2], t[i-1] + h)

    x[i] = r[0] + (k[0][0] + 2*k[1][0] + 2*k[2][0] + k[3][0])/6
    y[i] = r[1] + (k[0][1] + 2*k[1][1] + 2*k[2][1] + k[3][1])/6

plt.plot(t,x, 'r-')
plt.plot(t,y, 'b-')
plt.show()