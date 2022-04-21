from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm


def f(x):
    y = x**4 - 2*x + 1
    return y

x = np.linspace(0,2,100)

ans = mm.trapezoidal_integral(f, x)
print(ans)


def g(x):
    y = sin(x)
    return y

x2 = np.linspace(0, np.pi, 100)
ans_simplson = mm.simplson_rule(g,x2)
print(ans_simplson)


ans_simplson_38 = mm.simplsom_38_rule(g,x2)
print(ans_simplson_38)