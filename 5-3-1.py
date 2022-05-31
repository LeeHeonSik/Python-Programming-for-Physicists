from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return -x**3 + sin(t)


def Runge_Kutta(f,x,t):
    h = t[1] - t[0]
    for i in range(len(x)-1):
        k1 = h*f(x[i],t[i])
        k2 = h*f(x[i]+k1/2, t[i]+h/2)
        x[i+1] = x[i] + k2
    return x, t

t = np.linspace(0,10,1000)
x = np.zeros(len(t), float)

x,t = Runge_Kutta(f,x,t)
plt.plot(t,x)
plt.show()