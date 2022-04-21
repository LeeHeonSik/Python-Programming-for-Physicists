from math import *
import numpy as np
import matplotlib.pyplot as plt
# import my_module as mm

def f(x):
    y = exp(x)
    return y

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

x1 = np.linspace(0, 2.5, 101)
x2 = np.linspace(0, 2.5, 100)

simplson = simplson_rule(f,x1)
simplson_38 = simplsom_38_rule(f,x2)


print("1/3 : ", simplson)
print("8/3 : ", simplson_38)