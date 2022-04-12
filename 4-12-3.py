from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x - exp(1-x**2)
    return y

def dfdx(f,x,dx):
    y = (f(x) - f(x-dx))/dx
    return y



def SCM(f1,f2):
    tolerance = 1.0e-5
    delta = 1.0
    x1 = 0    #x1 = x_k
    dx = 0.1
    x2 = x1 - dx    # x2 = x_k-1
    while abs(delta) > tolerance:
        delta = -f1(x1)/f2(f1,x1,dx)
        x2 = x1
        x1 += delta
        dx = x1 - x2
    return x1

x = SCM(f,dfdx)
print("x : ", x)
