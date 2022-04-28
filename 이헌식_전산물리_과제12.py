from math import *
import numpy as np
import matplotlib.pyplot as plt
# import my_module as mm

def f(x,y):
    return 1/(x + (x**2 + 1)**(1/2)) - y/((x**2 + 1)**(1/2))

# def Picard_Method(f,x,t):
#     h = t[1] - t[0]
#     for i in range(len(x)-1):
#         predic = x[i] + f(x[i],t[i]) * h     ### x _ i + 1 EM 이용해서 구함
#         x[i+1] = x[i] + (h/2)*(f(x[i],t[i]) + f(predic, t[i+1]))
#     return x, t

y_0 = 0
x_0 = 0
x_max = 10

x = np.linspace(x_0, x_max, 1001)
y = np.zeros(len(x), float)

h = x[1] - x[0]
for i in range(len(x)-1):
    predic = y[i] + f(x[i],y[i]) * h     ### x _ i + 1 EM 이용해서 구함
    y[i+1] = y[i] + (h/2)*(f(x[i],y[i]) + f(x[i+1],predic))

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