from math import *
import numpy as np
import matplotlib.pyplot as plt

####################
#### HW1
def f(x):
    y = exp(x)*log(x) - x**2
    return y

def dfdx(x):
    y = exp(x)*log(x) + exp(x)/x - 2*x
    return y

px = []

tolerance = 1.0e-6
delta = 1.0
x = 1.5
while abs(delta) > tolerance:
    delta = -f(x)/dfdx(x)
    x += delta
print("x :", x)


###################
#### HW2
def f(x):
    y = x**5 - 3*x**4 - 5*x**3 - x**2 + x + 3
    return y

def dfdx(x):
    y = 5*x**4 - 12*x**3 - 15*x**2 - 2*x + 1
    return y

px = []

for x in range(-2,5,2):
    tolerance = 1.0e-6
    delta = 1.0
    while abs(delta) > tolerance:
        delta = -f(x)/dfdx(x)
        x += delta
    if x not in px:
        px.append(x)

print("x :",px)