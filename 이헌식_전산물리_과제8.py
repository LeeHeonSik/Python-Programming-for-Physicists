from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = exp(x)
    return y

x = np.linspace(0, 2.5, 100)
h = x[1] - x[0]
ans = 0.0

for i in range(len(x)-1):
    ans += f((x[i] + x[i+1])/2)

ans *= h
print(ans)