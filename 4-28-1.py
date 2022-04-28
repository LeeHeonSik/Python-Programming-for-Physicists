from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return -x**3 + sin(t)

t_0 = 0
t_max = 10
x_0 = 0

t = np.linspace(t_0, t_max, 1001)
x = np.zeros(len(t), float)

## solution
h = t[1] - t[0]
for i in range(len(t)-1):
    x[i+1] = x[i] + h * f(x[i], t[i])

# def Euler_Method(f,x,t):
#     h = t[1] - t[0]
#     for i in range(len(x)-1):
#         x[i+1] = x[i] + f(x[i], t[i]) * h
#     return x,t


plt.xlim(t_0, t_max)
plt.plot(t,x)
plt.xlabel(r"$t$")
plt.ylabel(r"$x(t)$")
plt.show()