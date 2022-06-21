import numpy as np
import random as rd
import matplotlib.pyplot as plt

def chi_sq(f,x,y,sigma,a,b):
    chi2 = 0
    for i in range(len(x)):
        chi2 += ((y[i] - f(x[i],a,b))/sigma[i])**2
    return chi2

def grad(f,g,x,y,sigma,a,b,h):
    fa = (f(lin_f,x,y,sigma,a+h,b) - f(lin_f,x,y,sigma,a-h,b))/(2*h)
    fb = (f(lin_f,x,y,sigma,a,b+h) - f(lin_f,x,y,sigma,a,b-h))/(2*h)
    return np.array([fa,fb])

def lin_f(x,a,b):
    return b*x + a

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

tolerance = 1.0e-5
epsilon = 1
param = np.array([1,1], float)
h = 0.001
eta = 0.0001

while tolerance<epsilon:
    delta = grad(chi_sq, lin_f, x, y, sigma, param[0], param[1], h)
    param -= eta * delta
    epsilon = np.max(np.abs(delta))

print(param)

fit_x = np.linspace(0,10,10)
fit_y = b * fit_x + a
fit_yp = param[1] * fit_x + param[0]


plt.plot(x,y,'ro', ms = 5)
plt.plot(fit_x, fit_y, 'b-')
plt.plot(fit_x, fit_yp, 'r--')
plt.show()