import numpy as np
import matplotlib.pyplot as plt

### cnst
L = 1.0
V = 20.0
hbar = 1.0
m = 1.0
N = 1000
h = L / N
e = 1.6e-19

### setting the fns
def V(x):
    if abs(x) <= L:
        return 0.0
    else:
        return V

def f(r,x,E):
    psi=r[0]
    phi=r[1]
    f_psi=phi
    f_phi=(2*m/hbar**2)*(V(x)-E)*psi
    return np.array([f_psi,f_phi],float)

### let's calculate
def RK4(r,x,E):
    k1=h*f(r,x,E)
    k2=h*f(r+k1/2,x+h/2,E)
    k3=h*f(r+k2/2,x+h/2,E)
    k4=h*f(r+k3,x+h,E)
    r+=(k1+2*k2+2*k3+k4)/6
    return r    ## r = [1.1]

def solve(E):
    psi=0
    phi=1
    r=np.array([psi,phi],float)
    for x in np.arange(0,L,h):
        r=RK4(r,x,E)
    return r[0]

#### find the energy
E1 = 0.0
E2 = e
psi2 = solve(E1)
tolerance = e/1000    ## 1.0e-6  >>>>> e = 1.6e-19
while abs(E2-E1) > tolerance: 
    psi1, psi2 = psi2, solve(E2)
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
    r = RK4(r,x,E2)
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
