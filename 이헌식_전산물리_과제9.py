from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = exp(x)
    return y

def trapezoidal_integral(f,x):
    h = x[1] - x[0]
    res = 0

    for i in range(len(x)-1):
        res += f(x[i]) + f(x[i+1])
    res *= h
    res /= 2
    return res


x = np.linspace(0, 2.5, 100)

ans = trapezoidal_integral(f,x)
print(ans)