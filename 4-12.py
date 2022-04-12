from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x - exp(1-x**2)
    return y

def dfdx(x):
    y = 1 + 2*x*exp(1-x**2)
    return y

# px = []
# x = 1.4
# px.append(x)

# for i in range(10):
#     delta = -f(x)/dfdx(x)
#     x += delta
#     px.append(x)

# plt.plot(px, 'ro')
# plt.show()

tolerance = 1.0e-6
delta = 1.0
x = 1.5
while abs(delta) > tolerance:
    delta = -f(x)/dfdx(x)
    x += delta
print("x :", x, "+/-", delta)