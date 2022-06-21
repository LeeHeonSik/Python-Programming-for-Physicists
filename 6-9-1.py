## fitting : 벗어나있는 정도의 평균(합)이 가장 작은 놈 찾기

import numpy as np
import matplotlib.pyplot as plt
import random as rd

x = np.array(range(1,10), float)
y = x*2 + 3
sigma = np.ones_like(x)

print(x, y)
for i in range(len(y)):
    y[i] += (rd.random() - 0.5) * 0.3
print("random y = ", y)

alpha = np.sum(1/sigma**2)
beta = 0
delta = 0
theta = 0
phi = 0
## page 9
for i in range(len(x)):
    beta += x[i]/sigma[i]**2
    delta += x[i]**2/sigma[i]**2
    theta += y[i]/sigma[i]**2
    phi += x[i]*y[i]/sigma[i]**2
gamma = beta
## page 10
D = alpha * delta - beta**2
a = (theta*delta - beta*phi) / D
b = (alpha * phi - gamma*theta) / D
## eq 8
delta_a = delta/D
delta_b = alpha/D


print("a =", a, "+/-", delta_a)
print("b =", b, "+/-", delta_b)

fit_x = np.linspace(0,10,10)
fit_y = b * fit_x + a



plt.plot(x,y,'ro', ms = 5)
plt.plot(fit_x, fit_y, 'b-')
plt.show()