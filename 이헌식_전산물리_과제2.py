from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = exp(x)*log(x) - x**2
    return y
# cnst
a, b = 1, 2
accuracy = 1e-6
error = 1.0

# start
while error > accuracy:
    x0 = (a+b)/2.0
    if f(a)*f(x0)<0:
        b = x0
    else:
        a=x0
    error = abs(a-b)
print(x0)