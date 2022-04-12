ans = [1, 1]
N = int(input(":"))
i = 2
while i < N:
    k = ans[i] + ans[i+1]
    ans.append(k)
    i += 1
print(ans)