from math import *
import numpy as np
import matplotlib.pyplot as plt

# def f(x):
#     y = x**4 - 2*x + 1
#     return y

# x = np.linspace(0,2,100)
# h = x[1] - x[0]   #step size
# inte_res = 0.0

# for i in range(len(x)-1):
#     inte_res += f((x[i]+x[i+1])/2)
# inte_res *= h                ### multiple length

# print(inte_res)


def f(x):
    y = sin(x)
    return y

x = np.linspace(0, np.pi, 100)
h = x[1] - x[0]

ans = 0.0
for i in range(len(x)-1):
    ans += f((x[i] + x[i+1])/2)
ans *= h
print(ans)