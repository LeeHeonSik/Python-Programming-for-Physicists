from matplotlib import pyplot as plt
import numpy as np

N = int(input("input the N: "))
x = [i for i in range(N)]
y = []
k = 0
for j in range(1, N+1):
    k += 1/j
    y.append(k)

plt.plot(x,y)
plt.xscale('log')
plt.show()