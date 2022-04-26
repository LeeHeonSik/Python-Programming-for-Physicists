from math import *
import numpy as np
import matplotlib.pyplot as plt

##### differential



##### 직사각형 적분
def rectangular_integral(f,x):
    h = x[1] - x[0]
    res = 0.0
    for i in range(len(x)-1):
        res += f((x[i] + x[i+1])/2)
    res *= h
    return res


##### 평행사변형 적분
def trapezoidal_integral(f,x):
    h = x[1] - x[0]
    res = 0

    for i in range(len(x)-1):
        res += f(x[i]) + f(x[i+1])
    res *= h
    res /= 2
    return res


##### Simplson's Rule
def simplson_rule(f,x):
    h = x[1] - x[0]
    res = 0

    for i in range(0, len(x)-2, 2):
        res += f(x[i+2]) + 4*f(x[i+1]) + f(x[i])
    
    res *=h
    res /= 3
    return res

def simplsom_38_rule(f,x):
    h =x[1] - x[0]
    res = 0

    for i in range(0,len(x)-3,3):
        res += f(x[i]) + 3*f(x[i+1]) + 3*f(x[i+2]) + f(x[i+3])
    res *= 3*h
    res /= 8
    return res