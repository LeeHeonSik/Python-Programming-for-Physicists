from math import *
import numpy as np
import matplotlib.pyplot as plt
# import my_module as mm

def f(x,y):
    return 1/(x + (x**2 + 1)**(1/2)) - y/((x**2 + 1)**(1/2))