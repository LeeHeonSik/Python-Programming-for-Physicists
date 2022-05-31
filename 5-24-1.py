from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

M = 100    ## 칸 갯수
V = [0, 1.0]
tolarence = 1.0e-5

phi = np.zeros([M+1, M+1], float)
phi[0,:] = V[1]
phitemp = np.zeros_like(phi, float)
phitemp = np.copy(phi)

h = 1/M
delta = 1.0
while delta > tolarence:
    for i in range(1,M):           ### boundary 건들지 않음 = 고정
        for j in range(1, M):
            phitemp[i][j] = (phi[i+1][j] + phi[i-1][j] + phi[i][j+1] + phi[i][j-1] - 0)/4   ## g = 0
    delta = np.max(abs(phi - phitemp))     # n 번째 값과 n+1 번째 값의 차이
    phi, phitemp = phitemp, phi


"""  boundary 컨디션 포함   예상문제 -> BC에 자꾸 부딪힐 때 예외처리 
while delta > tolarence:
    for i in range(0,M+1):          
        for j in range(0, M+1):
            if i ==0 or j == 0 or i == M or j == M:
                phitemp[i]j[] = phi[i][j]
            else:
                phitemp[i][j] = (phi[i+1][j] + phi[i-1][j] + phi[i][j+1] + phi[i][j-1] - 0)/4   ## g = 0
    delta = np.max(abs(phi - phitemp))     # n 번째 값과 n+1 번째 값의 차이
    phi, phitemp = phitemp, phi
"""

plt.imshow(phi)
plt.show()