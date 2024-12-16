n_x = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

i = 0
j = n_x[0] - 1
k = n_x[1]
count = 0
suma = 0
while i <= j:
    suma = suma + nums[i]
    if suma > k:
        count += 1
        suma = 0
        i -= 1
    i += 1
if suma > 0:
    count += 1
print(count)

