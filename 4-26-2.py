import numpy as np
import random as rd

def f(x):
    return np.sin(x)


N = 10**3

a = 0
b = np.pi
sum_f = 0

for i in range(N):
    sum_f += f(rd.random() * (b-a) + a)

res = (b-a) * sum_f / N
print(res)
