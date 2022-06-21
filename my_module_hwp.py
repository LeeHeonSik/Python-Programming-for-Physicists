from math import*

def f(x):
    return x**2+2*x-3

x=float(input("x="))
h=float(input("h="))

tol=e**-8

def bisec(x,h,tol):
    while abs(f(x))>tol:
        while f(x)*f(x+h)>0:
            x=x+h
        h=h/2
    print(x)

print(bisec(x,h,tol))