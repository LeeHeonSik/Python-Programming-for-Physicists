from math import *
import numpy as np
import matplotlib.pyplot as plt
import my_module_최적화 as mm
from scipy.optimize import curve_fit
## https://turtle-dennis.tistory.com/17


def f(x):
    y = sin(x)
    return y

N = int(input("N : "))        #### 보고 싶은 끝값 N을 입력받음
ans1, ans2, ans3, ans4 = [], [], [], []
x1, x2, x3, x4 = [], [], [], []
# real_ans = []
for i in range(10, N+1):
    k, _x1 = mm.rectangular_integral(f,i)
    ans1.append(abs(k-2))
    k, _x2 = mm.trapezoidal_integral(f,i)
    ans2.append(abs(k-2))
    k, _x3 = mm.simplson_rule(f,i)
    ans3.append(abs(k-2))
    k, _x4 = mm.simplsom_38_rule(f,i)
    ans4.append(abs(k-2))
    x1.append(len(_x1))
    x2.append(len(_x2))
    x3.append(len(_x3))
    x4.append(len(_x4))



## fitting
def func(x, a, b):
    y = a*x + b
    return y

ans1_log = np.log(ans1)
ans2_log = np.log(ans2)
ans3_log = np.log(ans3)
ans4_log = np.log(ans4)
x1_log = np.log(x1)
x2_log = np.log(x2)
x3_log = np.log(x3)
x4_log = np.log(x4)

popt1, pcov = curve_fit(func, x1_log, ans1_log, method = 'lm')
popt2, pcov = curve_fit(func, x2_log, ans2_log, method = 'lm')
popt3, pcov = curve_fit(func, x3_log, ans3_log, method = 'lm')
popt4, pcov = curve_fit(func, x4_log, ans4_log, method = 'lm')
print("rec :", popt1, "trape : ", popt2, "simplson : ", popt3, "38_simplson : ", popt4)
# plt.plot(x, func(x, *popt), label = 'fitting')
# plt.subplot(2,2,1)
plt.plot(x1, ans1, 'r-', label = "rectang", )
# # plt.plot(x, real_ans, 'b-')
# plt.title("rectang")
# # plt.xlim(10,N)
# # plt.ylim(-5,5)
# plt.xscale('log')
# plt.yscale('log')

# plt.subplot(2,2,2)
plt.plot(x2, ans2, 'm-', label = "trape")
# plt.plot(x, real_ans, 'b-')
# plt.title("trape")
# # plt.xlim(10,N)
# # plt.ylim(-5,5)
# plt.xscale('log')
# plt.yscale('log')

# plt.subplot(2,2,3)
plt.plot(x3, ans3, 'g-', label = "1/3 simplson")
# plt.plot(x, real_ans, 'b-')
# plt.title("1/3 simplson")
# # plt.xlim(10,N)
# # plt.ylim(-5,5)
# plt.xscale('log')
# plt.yscale('log')

# plt.subplot(2,2,4)
plt.plot(x4, ans4, 'y-', label = "8/3 simplson")
# plt.plot(x, real_ans, 'b-')
# plt.title("8/3 simplson")
# # plt.xlim(10,N)
# # plt.ylim(-5,5)
plt.xscale('log')
plt.yscale('log')
plt.legend()

plt.show()