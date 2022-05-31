from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

M = 25    ## 칸 갯수
V = [5, 10]
tolarence = 1.0e-6

phi = np.zeros([M+1, M+1], float)
phi[0,:] = phi[M,:] = phi[:,0] = phi[:,M] = V[1]         ### 외부 사각형
for i in range(6):
    phi[10][10+i] = phi[15][10+i] = phi[10+i][10] = phi[10+i][15] = V[0]  ### 내부 사각형  틀림

phitemp = np.zeros_like(phi, float)
phitemp = np.copy(phi)

h = 1/M
delta = 1.0

while delta > tolarence:
    for i in range(1,M):          
        for j in range(1, M):
            if 10<= i <= 15 and 10<= j <= 15:   #### BC 수정
                phitemp[i][j] = phi[i][j]
            else:
                phitemp[i][j] = (phi[i+1][j] + phi[i-1][j] + phi[i][j+1] + phi[i][j-1] - 0)/4   ## g = 0
    delta = np.max(abs(phi - phitemp))     # n 번째 값과 n+1 번째 값의 차이
    phi, phitemp = phitemp, phi



# while delta > tolarence:
#     for i in range(0,M+1):          
#         for j in range(0, M+1):
#             if (i == 0 or j == 0 or i == M or j == M) or (i == 10 or j == 10 or i == 15 or j == 15):   #### BC 수정
#                 phitemp[i][j] = phi[i][j]
#             else:
#                 phitemp[i][j] = (phi[i+1][j] + phi[i-1][j] + phi[i][j+1] + phi[i][j-1] - 0)/4   ## g = 0
#     delta = np.max(abs(phi - phitemp))     # n 번째 값과 n+1 번째 값의 차이
#     phi, phitemp = phitemp, phi

    
plt.imshow(phi)
plt.show()