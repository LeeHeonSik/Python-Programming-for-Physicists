from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = sin(x)
    return y

x = np.linspace(-2*np.pi, 2*np.pi, 100)
h = 1.0e-4

def d2fdx2(f,x,h):
    y = f(x+h)-2*f(x)+f(x-h)
    y /= h**2
    return y

ddf = np.zeros_like(x,float)
# print(ddf)

for i in range(len(x)):
    ddf[i] = d2fdx2(f, x[i], h)

anal = -np.sin(x)

plt.plot(x,ddf, 'ro', ms=4)
plt.plot(x,anal,'k-',lw=3)
plt.show()