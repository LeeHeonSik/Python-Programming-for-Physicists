from math import *
import numpy as np
import matplotlib.pyplot as plt
# import my_module as mm

def f(x,y):
    return 1/(x + (x**2 + 1)**(1/2)) - y/((x**2 + 1)**(1/2))

def Euler_Method(f,x,t):
    h = t[1] - t[0]
    for i in range(len(x)-1):
        x[i+1] = x[i] + f(x[i], t[i]) * h
    return x,t

y_0 = 0
x_0 = 0
y_max = 10

y = np.linspace(y_0, y_max, 1001)
x = np.zeros(len(y), float)

x_plot, y_plot = Euler_Method(f,x,y)

plt.plot(x_plot,y_plot)
plt.show()


### solution
### y(x) = c_1 e^(-sinh^(-1)(x)) + x e^(-sinh^(-1)(x))   / 