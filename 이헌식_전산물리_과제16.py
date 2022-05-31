from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

### first case or second case
start = int(input("1st or 2nd? :"))
if start == 1:
    omega_0, q, b = 2/3, 0.5, 0.9
elif start == 2:
    omega_0, q, b = 2/3, 0.5, 1.15


def f(r, t):      ### x = theta / dx/dt = v
    x = r[0]
    v = r[1]
    return -q*v - sin(x) + b*cos(omega_0 * t)

## initial cond'
t_i, t_f = 0.0, 100.0  ## == x_i

t = np.linspace(t_i, t_f, 1000)
x = np.zeros_like(t,float)
dim = 2
r = np.zeros([len(t), dim], float)    ######## 여기 뭐냐

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

r3, t  =Runge_kutta_4th(f,r,t,dim)

# plt.xlabel(r'$t$')
# plt.ylabel(r'$x(t)$, $\omega(t)$')
plt.plot(t,r3[:,0], 'g-')
# plt.legend()
plt.show()