from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

G = 9.81
t_i, t_f = 0.0, 10.0  ## == x_i

t = np.linspace(t_i, t_f, 1000)

def f(r,t):
    x = r[0]
    v = r[1]
    return np.array([v,-G],float)

def Runge_kutta_4th(f,x,t,h,dim):
    c = np.zeros([4,dim], float)  #c1 == c[0] 
    c[0] = h * f(x, t)
    c[1] = h * f(x + c[0]/2, t + h/2)
    c[2] = h * f(x + c[1]/2, t + h/2)
    c[3] = h * f(x + c[2], t + h)
    x += (c[0] + 2*c[1] + 2*c[2] + c[3])/6
    return x


def g(v,t):
    dim = 2
    r = np.array([0.0,v], float)
    h = t[1] - t[0]
    for i in range(len(t)-1):
        r = Runge_kutta_4th(f,r,t[i],h,2)

    return r[0] - 0.0       ##g(alpha) = 0

v1 = 0.001
v2 = 1000.0
tolerance = 10e-6               ### bisec 사용하기 위한 조건

h1 = g(v1, t)
h2 = g(v2, t)

while abs(v2 - v1) > tolerance:
    vm = (v1 + v2)/2
    hm = g(vm,t)
    if h1 * hm > 0:
        v1 = vm
        h1 = hm
    else:
        v2 = vm
        h2 = hm
v_i = (v1 + v2)/2
print(v_i)

x = np.zeros_like(t, float)
v = np.zeros_like(t, float)

x[0] = 0.0
v[0] = v_i
tau = t[1] - t[0]

r = np.array([0.0, v_i], float)
for i in range(1,len(t)):
    r = Runge_kutta_4th(f,r,t[i-1],tau,2)
    x[i] = r[0]
    v[i] = r[1]

plt.plot(t,x)
plt.show()