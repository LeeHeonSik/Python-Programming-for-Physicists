from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    print(x)
    return 2-exp(-x)
x0 = 1.0
x = 0
y = []
for i in range(10):
    x = f(x0)
    y.append(x)
    x0 = x

X = np.arange(0,10,1)
plt.plot(X,y)
plt.show()