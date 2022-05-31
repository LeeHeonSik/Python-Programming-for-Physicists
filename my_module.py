from math import *
import numpy as np
import matplotlib.pyplot as plt

##### differential



##### 직사각형 적분
def rectangular_integral(f,x):
    h = x[1] - x[0]
    res = 0.0
    for i in range(len(x)-1):
        res += f((x[i] + x[i+1])/2)
    res *= h
    return res


##### 평행사변형 적분
def trapezoidal_integral(f,x):
    h = x[1] - x[0]
    res = 0

    for i in range(len(x)-1):
        res += f(x[i]) + f(x[i+1])
    res *= h
    res /= 2
    return res


##### Simplson's Rule
def simplson_rule(f,x):
    h = x[1] - x[0]
    res = 0

    for i in range(0, len(x)-2, 2):
        res += f(x[i+2]) + 4*f(x[i+1]) + f(x[i])
    
    res *=h
    res /= 3
    return res

def simplsom_38_rule(f,x):
    h =x[1] - x[0]
    res = 0

    for i in range(0,len(x)-3,3):
        res += f(x[i]) + 3*f(x[i+1]) + 3*f(x[i+2]) + f(x[i+3])
    res *= 3*h
    res /= 8
    return res



 ####### diff Eq sol
### Euler
def Euler_Method(f,x,t):
    h = t[1] - t[0]
    for i in range(len(x)-1):
        x[i+1] = x[i] + f(x[i], t[i]) * h
    return x,t

### Predic
def Picard_Method(f,x,t):
    h = t[1] - t[0]
    for i in range(len(x)-1):
        predic = x[i] + f(x[i],t[i]) * h     ### x _ i + 1 EM 이용해서 구함
        x[i+1] = x[i] + (h/2)*(f(x[i],t[i]) + f(predic, t[i+1]))
    return x, t

### Runge-Kutta     dx/dt = f(x,t)
def Runge_Kutta_ver1(f,x,t):
    h = t[1] - t[0]
    for i in range(len(x)-1):
        k1 = h*f(x[i],t[i])
        k2 = h*f(x[i]+k1/2, t[i]+h/2)
        x[i+1] = x[i] + k2
    return x, t

def Runge_kutta_ver2(f,x,t):
    h = t[1] - t[0]
    a1 = 0.5
    a2 = 1-a1
    nu21 = (1/2) / a2
    for i in range(len(x)-1):
        c1 = h * f(x[i], t[i])
        c2 = h * f(x[i] + c1*nu21, t[i] + h*nu21)
        x[i+1] = x[i] + a1*c1+a2*c2
    return x, t

def Runge_kutta_4th(f,x,t,dim):
    c = np.zeros([4,dim], float)  #c1 == c[0] 
    h = t[1] - t[0]
    for i in range(len(x)-1):
        c[0] = h * f(x[i], t[i])
        c[1] = h * f(x[i] + c[0]/2, t[i] + h/2)
        c[2] = h * f(x[i] + c[1]/2, t[i] + h/2)
        c[3] = h * f(x[i] + c[2], t[i] + h)
        x[i+1] = x[i] + (c[0] + 2*c[1] + 2*c[2] + c[3])/6
    return np.array(x), t 

## 5/12 revisit Newton's Eq of motion  ch8. p57
def RK_4th_2ndOrder(f,x,v,t):
    c = np.zeros(4, float)
    h = t[1] - t[0]

    for i in range(len(t)-1):
        c[0] = h * f(x[i], v[i], t[i])
        c[1] = h * f(x[i] + h * v[i]/2, v[i] + c[0]/2, t[i] + h/2)
        c[2] = h * f(x[i] + h * v[i]/2 + h*c[0]/4, v[i] + c[1]/2, t[i] + h/2)
        c[3] = h * f(x[i] + h * v[i] + h*c[1]/2, v[i] + c[2], t[i] + h)
        
        x[i+1] = x[i] + h * v[i] + h*(c[0] + c[1] + c[2])/6
        v[i+1] = v[i] + (c[0] + 2*c[1] + 2*c[2] + c[3])/6
    return x, v


### DE more than one variable
#5-10-1.py
def DE_more_variable(f):
    t = np.linspace(0, 10, 1000)
    x = np.ones_like(t)
    y = np.ones_like(t)
    k = np.zeros([4,2], float)   ## k1 (=c1) with matrix

    h = t[1] - t[0]
    for i in range(1, len(t)):
        r = [x[i-1], y[i-1]]
        k[0] = h * f(r,t[i-1])
        k[1] = h * f(r + k[0]/2, t[i-1] + h/2)
        k[2] = h * f(r + k[1]/2, t[i-1] + h/2)
        k[3] = h * f(r + k[2], t[i-1] + h)

        x[i] = r[0] + (k[0][0] + 2*k[1][0] + 2*k[2][0] + k[3][0])/6
        y[i] = r[1] + (k[0][1] + 2*k[1][1] + 2*k[2][1] + k[3][1])/6

    return (t, x, y)