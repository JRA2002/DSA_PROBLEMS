str1 = input()

maxi = 1
curr = 1
for i in range(len(str1) - 1):
    if str1[i] == str1[i+1]:
        curr += 1
    else:
        curr = 1
    if curr > maxi:
        maxi = curr
print(maxi)