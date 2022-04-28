import numpy as np
from math import *
import random as rd

def F(x,y,z):
    return (x + y + z)

a, b = 0, 1
c, d = 0, 1
e, f = 0, 1
N = 10**3
_sum = 0

for i in range(N):
    _sum += F(rd.random()*(b-a) + a, rd.random()*(d-c) + c, rd.random()*(f-e) + e)

res = _sum * (b-a)*(d-c)*(f-e)/N
print(res)