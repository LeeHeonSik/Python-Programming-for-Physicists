from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**2
    return y

def dfdx_forward(f,x,h):
    y = (f(x+h)-f(x))/h
    return y

def dfdx_backward(f,x,h):
    y = (f(x)-f(x-h))/h
    return y

def dfdx_tree(f,x,h):
    y = (f(x+h)-f(x-h))/(2*h)
    return y


x = np.linspace(-2, 2, 100)
dydx_f = np.zeros(len(x),float)
dydx_b = np.zeros(len(x),float)
dydx_t = np.zeros(len(x),float)

i = 0
h = 0.1
for xx in x:
    dydx_t[i] = dfdx_tree(f,xx,h)
    dydx_f[i] = dfdx_forward(f,xx,h)
    dydx_b[i] = dfdx_backward(f,xx,h)
    i += 1

plt.plot(x,dydx_t, 'bo')
plt.plot(x,dydx_f, 'r>')
plt.plot(x,dydx_b, 'g<')
plt.plot(x,2*x,'p-')
plt.show()