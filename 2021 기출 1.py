import matplotlib.pyplot as plt
import numpy as np

m = 1.0
hbar = 1.0
e = 1.6022e-19
L = 1.0
energy_level = [1.0, 2.0, 5.5]
N = 1000
V0 = 20.0

def V(x):
    if abs(x) < L:
        return 0.0
    else:
        return V0


def f(r, x, E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return np.array([fpsi, fphi], float)


def RK_4th(f, r, x, E):
    k1 = h*f(r, x, E)
    k2 = h*f(r+k1/2, x+h/2, E)
    k3 = h*f(r+k2/2, x+h/2, E)
    k4 = h*f(r+k3, x + h, E)
    r += (k1 + 2*k2 + 2*k3 + k4)/6
    return r


def solve(E):
    psi = 0.0 # 초기값
    phi = 1.0 # 초기값
    r = np.array([psi, phi], float)
    for x in np.arange(-2*L, 2*L, h):
        r = RK_4th(f, r, x, E)
    return r[0]

for level, n in enumerate(energy_level):
    # main program to find the energy using the secant method
    h = L / N
    E1 = n - 0.5 # using scant method
    E2 = n + 0.5

    psi2 = solve(E1)

    tol = 1.0e-4
    while abs(E2 - E1) > tol:
        psi1, psi2 = psi2, solve(E2)
        E1, E2 = E2, E2 - psi2*(E2-E1)/(psi2-psi1)

    print("E=", E2, "V")

    # Calculate the psi

    ppsi = []
    pphi = []
    px = []

    ppsi.append(0.0)
    pphi.append(1.0) # 아무 초기값
    px.append(-2*L)

    r = np.array([ppsi[0], pphi[0]], float)

    for x in np.arange(-2*L, 2*L, h):
        r = RK_4th(f, r, x, E2)
        ppsi.append(r[0])
        pphi.append(r[1])
        px.append(x+h)

    # Normalize psi
    integ = 0.0
    for i in range(len(px)):
        integ += h*ppsi[i]**2
    norm_ppsi = ppsi / np.sqrt(integ)


    plt.plot(px, norm_ppsi, label=f'n={level+1}')

plt.xlim(-2*L, 2*L)
plt.ylim(-2, 5)
plt.plot(px, list(map(V, px)), label='potential')
plt.legend()
plt.show()
