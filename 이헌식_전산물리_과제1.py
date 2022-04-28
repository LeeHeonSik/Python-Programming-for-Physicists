from matplotlib import pyplot as plt

## graph about N
N1 = [10, 100, 1000, 10000]
y1 = []
y2 = []
for i in N1:
    j = 1
    s1 = 0
    s2 = 0
    while j <= i:
        s1 += 1/j
        s2 += (1/j)**2
        j+= 1
    y1.append(s1)
    y2.append(s2)

## graph about 1/N
N2 = []
for i in N1:
    N2.append(1/i)

print(N1,y1,'\n',N2,y2)

plt.subplot(131)
plt.plot(N1, y1, 'r')
plt.title(r'$S1 : \Sigma \frac{1}{n}, log scale$')
plt.xscale('log')

plt.subplot(132)
plt.plot(N1, y2, 'g')
plt.title(r'$S2 : \Sigma \frac{1}{n^2}$')

plt.subplot(133)
plt.plot(N2, y2, 'g')
plt.title(r'$S2 : \Sigma \frac{1}{n^2}, 1/N scale$')
plt.show()
