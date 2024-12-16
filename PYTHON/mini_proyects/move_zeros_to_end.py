lst = [1, 0, 2, 0, 4, 0, 6, 5]
listz = []
for i in lst:
    if i==0:
        lst.remove(i)
        lst.append(i)
print(lst)