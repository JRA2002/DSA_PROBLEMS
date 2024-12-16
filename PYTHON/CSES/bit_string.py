n = int(input())
res = 1
for _ in range(n):
    res = 2*res%(10**9 + 7)
print(res)