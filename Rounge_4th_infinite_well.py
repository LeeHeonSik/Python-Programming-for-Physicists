import matplotlib.pyplot as plt
import numpy as np

###### setting the cnst values
## 2 pi r = n lambda / n : 1 -> 2
L = 5.29e-11
N = 1000
h = L/N
e = 1.6e-19
m = 9.1e-31
hbar = 1.054e-34

### setting the potential and SE eq
def V(x):    ## |x| <= a
    if 0 <= x <= L:
        return 0.0
    else:
        return np.inf

def f(r,x,E):
    psi = r[0]          ### diff once
    phi = r[1]
    fpsi = phi
    fphi = (2*m/(hbar**2))*(V(x)-E)*psi
    return np.array([fpsi,fphi],float) 

### setting the fns
def RungeKutta2d(r,x,E):
    k1 = h*f(r,x,E) 
    k2 = h*f(r+0.5*k1, x+0.5*h,E)
    k3 = h*f(r+0.5*k2, x+0.5*h,E)
    k4 = h*f(r+k3, x+h,E)
    r = r + (k1 + 2*k2 + 2*k3 + k4)/6
    return r

def sol(E):
    psi = 0.0
    phi = 1.0
    r = np.array([psi,phi], float)

    for x in np.arange(0,L,h):
        r = RungeKutta2d(r,x,E)
    return r[0] - 0

#### find the energy
E1 = 0.0
E2 = e
psi2 = sol(E1)
tolerance = e/1000    ## 1.0e-6  >>>>> e = 1.6e-19
while abs(E2-E1) > tolerance: 
    psi1, psi2 = psi2, sol(E2)
    E1, E2 = E2, E2 - psi2*(E2-E1)/(psi2 - psi1)


## calculate the psi
ppsi = []
pphi = []
px = []

ppsi.append(0.0)
pphi.append(1.0)
px.append(0.0)

r = np.array([ppsi[0], pphi[0]], float)

for x in np.arange(0,L,h):
    r = RungeKutta2d(r,x,E2)
    ppsi.append(r[0])
    pphi.append(r[1])
    px.append(x + h)


#### normalization
integ = 0.0
for i in range(len(px)):
    integ += h*ppsi[i]**2
norm_ppsi = ppsi / np.sqrt(integ)

plt.plot(px, norm_ppsi)
plt.xlim(0,L)
plt.show()