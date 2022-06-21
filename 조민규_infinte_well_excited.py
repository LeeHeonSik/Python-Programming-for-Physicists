import numpy as np
import matplotlib.pyplot as plt

###### costants
m=9.1094e-31
hbar=1.0546e-34
e=1.6022e-19
N=1000
n=[1,2,3,4]  # quantum number
L=5.2918e-11  #Bohr radius


######## setting the potential and SE eq
def V(x):    ## |x| <= a
    if 0 <= x <= L:
        return 0.0
    else:
        return np.inf

def f(r,x,E):
    psi=r[0]
    phi=r[1]
    f_psi=phi
    f_phi=(2*m/hbar**2)*(V(x)-E)*psi
    return np.array([f_psi,f_phi],float)

######## calculate the wavefuntion for a particular Energy-
def RK4(r,x,E):
    k1=h*f(r,x,E)
    k2=h*f(r+k1/2,x+h/2,E)
    k3=h*f(r+k2/2,x+h/2,E)
    k4=h*f(r+k3,x+h,E)
    r+=(k1+2*k2+2*k3+k4)/6
    return r

def solve(E):
    psi=0
    phi=1
    r=np.array([psi,phi],float)
    for x in np.arange(0,l,h):
        r=RK4(r,x,E)
    return r[0]

xxx = []
ppx = []
for i in range(len(n)):

    l=5.2918e-11/n[i]
    h=l/N

    # main program to find the energy using the secant method
    E1=0
    E2=e
    psi2=solve(E1)
    # psi2=solve(E2)

    tolerance=e/1000
    while abs(E2-E1)>tolerance:
        psi1,psi2=psi2,solve(E2)
        E1,E2=E2,E2-psi2*(E2-E1)/(psi2-psi1)
    print("E=",E2/e,"eV")

    # calculate the psi
    ppsi=[]
    pphi=[]
    px=[]

    ppsi.append(0)
    pphi.append(1)
    px.append(0)

    r=np.array([ppsi[0],pphi[0]],float)

    for x in np.arange(0,L,h):
        r=RK4(r,x,E2)
        ppsi.append(r[0])
        pphi.append(r[1])
        px.append(x+h)

    # normalize psi
    integral=0
    for i in range(len(px)):
        integral+=h*ppsi[i]**2
    norm_ppsi=ppsi/np.sqrt(integral)
    xxx.append(norm_ppsi)
    ppx.append(px)
    # plt.plot(px,norm_ppsi)
    # plt.xlim(0,L)
    # plt.ylim(-1,1)



######################### plot ####################
plt.subplot(2,2,1)
plt.plot(ppx[0], xxx[0], 'y-')
# plt.axhline(y = 0, color = 'k')
plt.xlim(0,L)
plt.title("n = 1")
plt.subplot(2,2,2)
plt.plot(ppx[1], xxx[1], 'g-')
plt.axhline(y = 0, color = 'k')
plt.xlim(0,L)
plt.title("n = 2")
plt.subplot(2,2,3)
plt.plot(ppx[2], xxx[2], 'b-')
plt.axhline(y = 0, color = 'k')
plt.xlim(0,L)
plt.title("n = 3")
plt.subplot(2,2,4)
plt.plot(ppx[3], xxx[3], 'r-')
plt.axhline(y = 0, color = 'k')
plt.xlim(0,L)
plt.title("n = 4")
plt.show()

##### plot all things together
plt.plot(ppx[0], xxx[0], 'y-', label= 'n = 1')
plt.plot(ppx[1], xxx[1], 'g-', label= 'n = 2')
plt.plot(ppx[2], xxx[2], 'b-', label= 'n = 3')
plt.plot(ppx[3], xxx[3], 'r-', label= 'n = 4')
plt.axhline(y = 0, color = 'k')
plt.legend()
plt.show()