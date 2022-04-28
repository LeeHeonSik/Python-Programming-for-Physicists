from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**5 - 3*x**4 - 5*x**3 - x**2 + x + 3
    return y

def dfdx(f,x,dx):
    y = (f(x) - f(x-dx))/dx
    return y



def SCM(f1,f2):
    ans = []
    x = [-2, 3, 4]
    for xx in x:
        tolerance = 1.0e-6
        delta = 1.0
        x1 = xx    #x1 = x_k
        dx = 0.1
        x2 = x1 - dx    # x2 = x_k-1
        while abs(delta) > tolerance:
            delta = -f1(x1)/f2(f1,x1,dx)
            x2 = x1
            x1 += delta
            dx = delta
        ans.append(x1)
    return ans


x = SCM(f,dfdx)
print("x : ", x)