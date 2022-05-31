from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

g = 9.81

l = 0.1

def f(theta, omega,t):
    f_omega = -g/l*sin(theta)
    return f_omega

def RK_4th_2ndOrder(f,x,v,t):
    c = np.zeros(4, float)
    h = t[1] - t[0]

    for i in range(len(t)-1):
        c[0] = h * f(x[i], v[i], t[i])
        c[1] = h * f(x[i] + h * v[i]/2, v[i] + c[0]/2, t[i] + h/2)
        c[2] = h * f(x[i] + h * v[i]/2 + h*c[0]/4, v[i] + c[1]/2, t[i] + h/2)
        c[3] = h * f(x[i] + h * v[i] + h*c[1]/2, v[i] + c[2], t[i] + h)
        
        x[i+1] = x[i] + h * v[i] + h*(c[0] + c[1] + c[2])/6
        v[i+1] = v[i] + (c[0] + 2*c[1] + 2*c[2] + c[3])/6
    return x, v
        

t = np.linspace(0.0, 5, 1000)
theta = np.zeros_like(t, float)
omega = np.zeros_like(t, float)

theta[0]= np.pi-0.1   ### 균형 깨뜨리기
omega[0]= 0.0

theta, omega = RK_4th_2ndOrder(f,theta, omega, t)
        
plt.plot(t, theta, 'r-')
plt.plot(t, omega, 'b-')
plt.show()