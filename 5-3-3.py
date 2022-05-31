from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(y,t):   ## dy/dt
    return -y**3 + sin(t)

def Runge_kutta_4th(f,x,t):
    c = np.zeros(4, float)  #c1 == c[0] 
    h = t[1] - t[0]
    for i in range(len(x)-1):
        c[0] = h * f(x[i], t[i])
        c[1] = h * f(x[i] + c[0]/2, t[i] + h/2)
        c[2] = h * f(x[i] + c[1]/2, t[i] + h/2)
        c[3] = h * f(x[i] + c[2], t[i] + h)
        x[i+1] = x[i] + (c[0] + 2*c[1] + 2*c[2] + c[3])/6
    return x, t 

t = np.linspace(0,10,1000)
x = np.zeros(len(t), float)

x,t = Runge_kutta_4th(f,x,t)


plt.plot(t,x, 'r-', label = "coding")
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.legend()
plt.show()