from math import *
import numpy as np
import matplotlib.pyplot as plt

m = k = 1
c = [8, 2, 0.4]   #### over, critical, under / using ind variable

def f(r, t):
    x = r[0]
    omega = r[1]
    f_x = omega
    f_omega = -ind/m * omega - k/m * x
    return np.array([f_x, f_omega])

def Runge_kutta_4th(f,x,t,dim):
    c = np.zeros([4,dim], float)  #c1 == c[0] 
    h = t[1] - t[0]
    for i in range(len(x)-1):
        c[0] = h * f(x[i], t[i])
        c[1] = h * f(x[i] + c[0]/2, t[i] + h/2)
        c[2] = h * f(x[i] + c[1]/2, t[i] + h/2)
        c[3] = h * f(x[i] + c[2], t[i] + h)
        x[i+1] = x[i] + (c[0] + 2*c[1] + 2*c[2] + c[3])/6
    return np.array(x), t

t = np.linspace(0.0, 15, 1000)
dim = 2
r = np.zeros([len(t), dim], float)

r[0][0] = np.pi-0.1   ### 균형 깨뜨리기
r[0][1] = 0.0

ind = c[0]
r1, t = Runge_kutta_4th(f,r,t,dim)
ind = c[1]
r2, t = Runge_kutta_4th(f,r,t,dim)
ind = c[2]
r3, t  =Runge_kutta_4th(f,r,t,dim)

plt.xlabel(r'$t$')
plt.ylabel(r'$x(t)$, $\omega(t)$')
plt.plot(t,r1[:,0], 'r-', label = r'$over$')
plt.plot(t,r2[:,0], 'b-', label = r'$critical$')
plt.plot(t,r3[:,0], 'g-', label = r'$under$')
plt.legend()
plt.show()