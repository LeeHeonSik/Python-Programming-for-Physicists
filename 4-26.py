import random as rd
import numpy as np
import matplotlib.pyplot as plt

Ntot = 10**3
Ncircle = 0
xx, yy = [], []
for i in range(Ntot):
    x = rd.random()
    y = rd.random()
    xx.append(x)
    yy.append(y)
    if y <= (1-x**2)**(1/2):
        Ncircle += 1
    
p = Ncircle / Ntot  
pi = 4 * p
print(pi)

xx_circle = []
yy_circle = []
for i in np.linspace(0, np.pi/2, 100):
    xx_circle.append(np.cos(i))
    yy_circle.append(np.sin(i))

plt.plot(xx,yy, 'o', ms = 1)
plt.plot(xx_circle, yy_circle, 'r-')

plt.show()