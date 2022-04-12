import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-np.pi, np.pi, 100)
# y = np.sin(x)

# plt.plot(x,y)
# plt.show()

# ## data = np.loadtxt("./name.txt", float)


# my_file = open("test.dat", "w")
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.cos(x)

# for i in range(len(x)):
#     print("%e %e" %(x[i], y[i]), file=my_file)
# my_file.close()

# with open("./test.dat", 'r') as f:
#     data = f.read()
# # print(data, type(data))
# data = data.split()
# # print(data)
# x = []
# y = []
# for i in range(0, len(data), 2):
#     x.append(data[i])
#     y.append(data[i+1])
# plt.plot(x,y)
# plt.xlabel("$\sigma$")
# plt.ylabel("$cos(t)$")
# plt.show()


import matplotlib


import matplotlib.pyplot as plt


from matplotlib.ticker import MultipleLocator

# #################################################

#   Setting for global variables

# #################################################

plt.style.use("classic")

plt.rcParams['axes.linewidth']=2

plt.rcParams['xtick.major.width']=2


plt.rcParams['ytick.major.width']=2


plt.rcParams['xtick.minor.width']=2



plt.rcParams['ytick.minor.width']=2

plt.rcParams['legend.frameon']=False

plt.rcParams['font.family'] = "Serif" #'DejaVu Serif'

#plt.rcParams['text.usetex']=True

plt.rcParams['legend.labelspacing']=0.05

#plt.rcParams['legend.columnspacing']=0.01

matplotlib.rc('xtick',labelsize=18)

matplotlib.rc('ytick',labelsize=18)

###################################################



from pylab import imshow,show
from numpy import loadtxt

data = loadtxt("circular.txt",float)
imshow(data)
show()