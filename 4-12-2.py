from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x,u):
    return tanh(x) - u

def dfdx(x):
    return 1/cosh(x)**2

ulist = np.linspace(-0.99,0.99,100)
px = []

for u in ulist:
    tolerance = 1.0e-6
    delta = 1.0
    x = 0
    while abs(delta) > tolerance:
        delta = -f(x,u)/dfdx(x)
        x += delta
    px.append(x)

plt.plot(ulist,px,'bo')
plt.show()