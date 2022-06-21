import matplotlib.pyplot as plt
import numpy as np

##### setting cnst ####
L = 1.0
V0 = 20.0
hbar = 1.0
m = 1.0
e = 1.602e-19
number= [1.0, 2.0]
N = 1000

#### setting the potential and SE ####
def V(x):
    if abs(x) < L:
        return 0.0
    else:
        return V0

def f(r, x, E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m / hbar**2) * (V(x)-E) * psi
    return np.array([fpsi, fphi], float)

def RK_4th(f, r, x, E):
    k1 = h*  f(r, x, E)
    k2 = h * f(r + k1 / 2, x + h / 2, E)
    k3 = h * f(r + k2 / 2, x + h / 2, E)
    k4 = h * f(r + k3, x + h, E)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return r     #r = [ , ]

def sol(E):
    psi = 0.0 
    phi = 1.0 
    r = np.array([psi, phi], float)

    for x in np.arange(-1.8*L, 1.8*L, h):
        r = RK_4th(f, r, x, E)
    return r[0]


#### main code ####
xxx = []
ppx = []
for n in number:
    h = L / N
    E1 = n - 0.3 # using scant method
    E2 = n + 0.3
    psi2 = sol(E1)
    tol = 1.0e-5
    
    while abs(E2 - E1) > tol:
        psi1, psi2 = psi2, sol(E2)
        E1, E2 = E2, E2 - psi2 * (E2-E1) / (psi2-psi1)
    print("E =" , E2, "V") # eV = e * V

    # calculate the psi
    ppsi = []
    pphi = []
    px = []
    ppsi.append(0.0)
    pphi.append(1.0)
    px.append(-1.8*L)

    r = np.array([ppsi[0], pphi[0]], float)

    for x in np.arange(-1.8*L, 1.8*L, h):
        r = RK_4th(f, r, x, E2)
        ppsi.append(r[0])
        pphi.append(r[1])
        px.append(x+h)

    # normalization
    integ = 0.0
    for i in range(len(px)):
        integ += h*ppsi[i]**2
    norm_ppsi = ppsi / np.sqrt(integ)

    #save the values for plot
    xxx.append(norm_ppsi)
    ppx.append(px)


######################### plot ####################
plt.figure(figsize=(6,8))

plt.subplot(2,1,1)
plt.plot(ppx[0], xxx[0], 'b-', label = 'SE')
# plt.axvline(x = 0, color = 'k')
# plt.axhline(y = 0, color = 'k')
plt.vlines(L, 0, 5, color = 'r', label = 'potential well')
plt.vlines(-L, 0, 5, color = 'r')
plt.hlines(0, -L, L, color = 'r')   # plot the potential
plt.xlim(-1.8*L,1.8*L)
plt.ylim(-2, 4)
plt.legend()
plt.title("n = 1, lowest even parity")

plt.subplot(2,1,2)
plt.plot(ppx[1], xxx[1], 'g-', label = 'SE')
plt.vlines(L, 0, 5, color = 'r', label = 'potential well')
plt.vlines(-L, 0, 5, color = 'r')
plt.hlines(0, -L, L, color = 'r')
plt.xlim(-1.8*L,1.8*L)
plt.ylim(-2, 4)
plt.legend()
plt.title("n = 2, lowest odd parity")

plt.show()