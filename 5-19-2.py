from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

def f(r,t):
    # x = r[0]
    # v = r[1]
    return -G

G = 9.81
t_i, t_f = 0.0, 10.0  ## == x_i

t = np.linspace(t_i, t_f, 100)

x = np.zeros_like(t,float)
x[0] = x[len(x)-1] = 0.0

x_tmp = np.zeros_like(x,float)
h = t[1] - t[0]

for n in range(100):
    for k in range(1, len(t)-1):
        x_tmp[k] = (x[k+1] + x[k-1] - h**2*f(x[k], t[k]))/2
    for k in range(1, len(t)-1):
        x[k] = x_tmp[k]

plt.plot(t,x)
plt.show()