import numpy as np
import matplotlib.pyplot as plt

### cnst
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2 * k - m*omega**2

### make the original matrix
A = np.zeros([N,N], float)
for i in range(N-1):
    A[i,i] = alpha
    A[i,i+1] = -k
    A[i+1,i] = -k
A[0,0] -= k
A[N-1,N-1] = alpha - k

v = np.zeros(N, float)
v[0] = C

xx = np.linalg.solve(A,v)

### perform the Gauss - Jordan Elimination
for i in range(N-1):
    ## 앞 숫자 1로 만들기
    div = A[i,i]
    #A[i,i] /= div
    A[i,i+1] /=div
    v[i] /= div

    if i == N-2:
        n = 2
    else:
        n = 3
    a_tmp = A[i+1,i]
    for j in range(n):
        A[i+1,i+j] -= A[i,i+j] * a_tmp
    v[i+1] -= v[i] * a_tmp

## last element
v[N-1] /= A[N-1,N-1]

### back substitution
x = np.zeros(N,float)
x[N-1] = v[N-1]
for i in range(N-2, -1, -1):
    x[i] = v[i] - A[i,i+1] * x[i+1]

## plot
plt.plot(x)
plt.plot(x, "ko", ms = 15)
plt.plot(xx, 'rs')
plt.show()