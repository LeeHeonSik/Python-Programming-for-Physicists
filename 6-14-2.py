import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi, 10)
y = np.sin(x)

def p(k,x,xk):
    pp = 1.0
    for i in range(len(xk)):
        if i != k:
            pp *= (x - xk[i]) / (xk[k]-xk[i])
    return pp

xxx = np.linspace(0,2*np.pi, 50)
P_x = []

for xx in xxx:
    yy = 0
    for k in range(len(x)):
        yy += p(k,xx,x) * y[k]
    
    P_x.append(yy)


plt.plot(x,y,'ro')
plt.plot(xxx,P_x, 'b--')
plt.plot(xxx, np.sin(xxx), 'r-')

plt.show()