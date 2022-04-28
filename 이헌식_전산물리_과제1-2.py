from matplotlib import pyplot as plt

N = int(input("input the N(10, 100, 1000, 10000) :"))
x2 = [x2 for x2 in range(1,N+1)]
y2 = []
j = 1
_sum2 = 0
while j <= N:
    _sum2 += 1/(j**2)
    y2.append(_sum2)
    j += 1

plt.plot(x2, y2, 'r')
plt.xscale('log')
plt.show()