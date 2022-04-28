from math import *
import numpy as np
import matplotlib.pyplot as plt
# import my_module as mm

def f(x,y):
    return 1/(x + sqrt(x**2 + 1)) - y/(sqrt(x**2 + 1))

# def Euler_Method(f,x,t):
#     h = t[1] - t[0]
#     for i in range(len(x)-1):
#         x[i+1] = x[i] + f(x[i], t[i]) * h
#     return x,t

y_0 = 0
x_0 = 0
x_max = 10

x = np.linspace(x_0, x_max, 1001)
y = np.zeros(len(x), float)

h = x[1] - x[0]
for i in range(len(x)-1):
    y[i+1] = y[i] + h * f(x[i], y[i])
# x_plot, t_plot = Euler_Method(f,x,t)


### solution
def sol(x):
    y = np.zeros(len(x)-1, float)
    for i in range(1, len(x)-1):
        y[i] = x[i]*exp(-np.arcsinh(x[i]))
    return y


plt.plot(x,y, 'r-', label = "coding")
plt.plot(x[1::], sol(x), 'b-', label = 'hand')
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.legend()
plt.show()


### solution
### y(x) = c_1 e^(-sinh^(-1)(x)) + x e^(-sinh^(-1)(x))   / 