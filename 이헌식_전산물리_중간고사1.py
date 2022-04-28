from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

######### 적분 함수
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
    for i in range(0, len(x)-3, 2):
        res += f(x[i+2]) + 4*f(x[i+1]) + f(x[i])
    
    res *=h
    res /= 3
    return res

def simplsom_38_rule(f,x):
    h =x[1] - x[0]
    res = 0
    for i in range(0,len(x)-5,3):
        res += f(x[i]) + 3*f(x[i+1]) + 3*f(x[i+2]) + f(x[i+3])
    res *= 3*h
    res /= 8
    return res


######
def f(X):
    return sin(X)

N = int(input("N : "))        #### 보고 싶은 끝값 N을 입력받음

ans1, ans2, ans3, ans4 = [], [], [], []

for i in range(10,N):
    x = np.linspace(0,i,100)
    ans1.append(abs(rectangular_integral(f,x)-2))
    ans2.append(abs(trapezoidal_integral(f,x)-2))
    ans3.append(abs(simplson_rule(f,x)-2))
    ans4.append(abs(simplsom_38_rule(f,x)-2))

## fitting
def func(x, a, b):
    y = a*x + b
    return y

_x = np.arange(10,N)

x_log = np.log(_x)
ans1_log = np.log(ans1)
ans2_log = np.log(ans2)
ans3_log = np.log(ans3)
ans4_log = np.log(ans4)
popt1, pcov = curve_fit(func, x_log, ans1_log, method = 'lm')
popt2, pcov = curve_fit(func, x_log, ans2_log, method = 'lm')
popt3, pcov = curve_fit(func, x_log, ans3_log, method = 'lm')
popt4, pcov = curve_fit(func, x_log, ans4_log, method = 'lm')
print(popt1, popt2, popt3, popt4)


##### plot
plt.plot(_x, ans1, 'r-', label = "rectang", )
plt.plot(_x, ans2, 'm-', label = "trape")
plt.plot(_x, ans3, 'g-', label = "1/3 simplson")
plt.plot(_x, ans4, 'y-', label = "8/3 simplson")
plt.xscale('log')
plt.yscale('log')
plt.legend()

plt.show()