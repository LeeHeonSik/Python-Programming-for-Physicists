from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

M = 100    ## 칸 갯수
V = [0, 1.0]
tolarence = 1.0e-2

phi = np.zeros([M+1, M+1], float)
phitemp = np.zeros_like(phi, float)
phitemp = np.copy(phi)
rho = np.zeros([M+1, M+1], float)

for i in range(60,80):
    for j in range(20,40):
        rho[i,j] = 1.0
        rho[j,i] = -1.0

h = 1/M
delta = 1.0
while delta > tolarence:
    for i in range(1,M):           ### boundary 건들지 않음 = 고정
        for j in range(1, M):
            phitemp[i][j] = (phi[i+1][j] + phi[i-1][j] + phi[i][j+1] + phi[i][j-1] - rho[i,j]*h**2)/4   ## g = 0
    delta = np.max(abs(phi - phitemp))     # n 번째 값과 n+1 번째 값의 차이
    phi, phitemp = phitemp, phi

plt.imshow(phi)
plt.show()