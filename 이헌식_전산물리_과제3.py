from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**5 - 3*x**4 - 5*x**3 + x**2 + x + 3
    return y

#cnst
a, b = -2, 4
# print(f(a),f(b)) = -35, - 41
# for i in range(a,b+1):
#     print(f(i))
# -35 4 3 -2 -47 -120 -41
# so, we choose a1 = -2, b1 = -1  /  a2 = 0, b2 = 1
a1, b1 = -2, -1
a2, b2 = 0, 1

#solve
def solve(a,b):
    accurancy = 1e-6
    error = 1.0
    while error > accurancy:
        x0 = (a+b)/2
        if f(a)*f(x0)<0:
            b = x0
        else:
            a=x0
        error = abs(a-b)
    return x0

#start
ans1 = solve(a1,b1)
ans2 = solve(a2,b2)
print("ans1 :", ans1,'\n',"ans2 : ", ans2)