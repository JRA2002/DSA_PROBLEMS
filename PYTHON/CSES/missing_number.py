n = int(input())
m = input().split()

suma = 0
for num in m:
    suma += int(num)
res = n*(n+1)//2 - suma
print(res)
