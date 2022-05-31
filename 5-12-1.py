from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

g = 9.81

l = 0.1

def f(r,t):
    theta = r[0]
    omega = r[1]
    f_theta = omega
    f_omega = -g/l*sin(theta)
    return np.array([f_theta, f_omega])

t = np.linspace(0.0, 5, 1000)
dim = 2
r = np.zeros([len(t), dim], float)

r[0][0] = np.pi-0.1   ### 균형 깨뜨리기
r[0][1] = 0.0

h = t[1] - t[0]

r, t = mm.Runge_kutta_4th(f,r,t,dim)

plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$, $\omega(t)$')
plt.plot(t,r[:,0], 'r-', label = r'$theta$')
plt.plot(t,r[:,1], 'b-', label = r'$omega$')
plt.legend()
plt.show()

plt.plot(r[:,0], r[:,1], 'r')
plt.show()