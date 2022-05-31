from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(y,t):   ## dy/dt
    return -y**3 + sin(t)

def Runge_kutta_ver2(f,x,t):
    h = t[1] - t[0]
    a1 = 0.5
    a2 = 1-a1
    nu21 = (1/2) / a2
    for i in range(len(x)-1):
        c1 = h * f(x[i], t[i])
        c2 = h * f(x[i] + c1*nu21, t[i] + h*nu21)
        x[i+1] = x[i] + a1*c1+a2*c2
    return x, t

t = np.linspace(0,10,1000)
x = np.zeros(len(t), float)

x,t = Runge_kutta_ver2(f,x,t)


plt.plot(t,x, 'r-', label = "coding")
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.legend()
plt.show()