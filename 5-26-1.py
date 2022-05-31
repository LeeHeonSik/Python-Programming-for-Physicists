from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm

A = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
v = np.array([-4,3,9,7],float)

M = len(v)

for i in range(M):
    div = A[i,i]      ##  맨 앞 숫자 1로 만들어주기
    A[i,:]/= div
    v[i] /= div
    for j in range(i+1, M):      # j in also an index for rows
        mul = A[j,i]
        A[j,:] -= mul * A[i,:]      ### A[i,:] == Ath row []
        v[j] -= mul * v[i]
print(A, '\n', "v = ", v)

# back substitution

x = np.zeros_like(v, float)

for i in range(M-1, -1, -1):
    x[i] = v[i]
    for j in range(i+1, M):
        x[i] -= A[i,j] * x[j]       ## x_i = v[i] - sigma(a[i,j] *x[j])

print("x = ", x)