from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**2
    return y

x = np.linspace(-2, 2, 100)
h = 0.01

def d2fdx2(f,x,h):
    y = f(x+h)-2*f(x)+f(x-h)
    y /= h**2
    return y

ddf = np.zeros_like(x,float)
print(ddf)

for i in range(len(x)):
    ddf[i] = d2fdx2(f, x[i], h)

anal = [2]*len(x)

plt.plot(x, ddf, 'ro', ms=4)
plt.plot(x, anal, 'k-', lw=3)
plt.ylim(0,3)
plt.show()