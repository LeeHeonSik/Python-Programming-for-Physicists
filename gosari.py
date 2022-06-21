x0=0.0; y0=0.0
n=0
from random import*

# p=open("gosari1.dat",'w+')

# while n<1000000:
#     n=n+1;a=randint(1,100)
#     if a<2:
#         x0,y0=0,0.16*y0
#     elif 1<a<87:
#         x0,y0= 0.85*x0+0.04*y0+0.00,-0.04*x0+0.85*y0+1.60
#     elif 86<a<94:
#         x0,y0=0.20*x0-0.26*y0+0.00,0.23*x0+0.22*y0+1.60
#     else:
#         x0,y0=-0.15*x0+0.28*y0+0.00,0.26*x0+0.24*y0+0.44
#     p.writelines("%f %f \n" %(x0,y0))

# p.close()

with open ('./gosari1.dat', 'r') as f:
    data = f.readlines()

xs, ys= [], []
data = map(lambda line:line.strip().split(' '), data)
# print(list(data)[:10])
data = list(data)
i = 0
while i < len(data):
    try: x,y = data[i]
    except: 
        i += 1
        continue
    xs.append(float(x))
    ys.append(float(y))
    i += 1  
from matplotlib import pyplot as plt

plt.scatter(xs, ys, c = ys, s = 20, alpha = 0.5, cmap = plt.cm.Greens)
plt.show()