from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

def f(x,v,t):
    mu, omega = 1.0, 1.0
    x_0 = 1.0
    return mu*(x_0**2  -x**2)*v - omega**2*x

def RK4th(f,r,h,tmax):
    x = []
    v = []
    t = []
    tt=0.0
    x.append(r[0])
    v.append(r[1])
    t.append(tt)
    c = np.zeros(4, float)
    i = 0
    while tt < tmax:
        c[0] = h * f(x[i], v[i], t[i])
        c[1] = h * f(x[i] + h*v[i]/2, v[i] + c[0]/2, t[i] + h/2)
        c[2] = h * f(x[i] + h*v[i]/2 + h*c[0]/4, v[i] + c[1]/2, t[i] + h/2)
        c[3] = h * f(x[i] + h*v[i] + h*c[1]/2, v[i] + c[2], t[i] + h)
        xx = x[i] + h*v[i] + h*(c[0] + c[1] + c[2])/6
        vv = v[i] + (c[0] + 2*c[1] + 2*c[2] + c[3])/6
        x.append(xx)
        v.append(vv)
        tt += h
        t.append(tt)
        i += 1
    
    return t, x, v


h = 0.01

t,x,v = RK4th(f,[1,1], h, 50.0)

plt.plot(t,x)
plt.plot(t,v)
plt.show()

plt.plot(x,v)
plt.show()