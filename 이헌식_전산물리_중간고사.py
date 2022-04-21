from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module as mm
from scipy.optimize import curve_fit
## https://turtle-dennis.tistory.com/17

def f(x):
    y = sin(x)
    return y

N = int(input())        #### 보고 싶은 끝값 N을 입력받음
ans1, ans2, ans3, ans4 = [], [], [], []
for i in range(1, N+1):
    x = np.linspace(0, np.pi, N)
    ans1.append(mm.rectangular_integral(f,x))
    ans2.append(mm.trapezoidal_integral(f,x))
    ans3.append(mm.simplson_rule(f,x))
    ans4.append(mm.simplsom_38_rule(f,x))

real_ans = [2] * N



plt.plot(x, ans1, 'r-')
plt.plot(x, real_ans, 'b-')
plt.xscale('log')
plt.yscale('log')
plt.show()