from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return -x**3 + sin(t)


def Picard_Method(f,x,t):
    h = t[1] - t[0]
    for i in range(len(x)-1):
        predic = x[i] + f(x[i],t[i]) * h     ### x _ i + 1 EM 이용해서 구함
        x[i+1] = x[i] + (h/2)*(f(x[i],t[i]) + f(predic, t[i+1]))
    return x, t

t_0 = 0
t_max = 10
x_0 = 0

t = np.linspace(t_0, t_max, 1001)
x = np.zeros(len(t), float)
x_plot, t_plot = Picard_Method(f,x,t)

plt.plot(t,x)
plt.show()