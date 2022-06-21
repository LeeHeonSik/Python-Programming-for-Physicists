import numpy as np

A = np.array([[1,4,8,4], [4,2,3,7], [8,3,6,9], [4,7,9,2]], float)

xx, VV = np.linalg.eigh(A)    ## eigenvalues
print("lambdas = ", xx)
print("eigenvectors = ", VV)

# step1
V = np.zeros_like(A,float)
N = V.shape[0]
#step2
for i in range(N):
    V[i,i] = 1
#step3
epsilon = 1.0e-10
#step4
Q = np.zeros_like(A,float)
R = np.zeros_like(A,float)
U = np.zeros_like(A,float)

delta = 1
while delta > epsilon:
    for i in range(N):
        U[:,i] = A[:,i]
        for j in range(i):
            U[:,i] -= np.dot(Q[:,j], A[:,i]) * Q[:,j]
        magui = np.dot(U[:,i],U[:,i])**(1/2)
        Q[:,i] = U[:,i] / magui    ### ith column
    
    for i in range(N):
        for j in range(N):
            if j == i:
                R[i,j] = np.dot(U[:,i], U[:,i])**(1/2)
            elif j > i:
                R[i,j] = np.dot(A[:,j], Q[:,i])
            else:
                R[i,j] = 0
    
    A = np.dot(R,Q)
    V = np.dot(V,Q)

    delta = 0.0
    for i in range(N):
        for j in range(N):
            if i != j:
                if delta < abs(A[i,j]):
                    delta = abs(A[i,j])
print("A : ", A)
print("V = ", V)