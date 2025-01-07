'''Given an array of size N, find the number of distinct pairs {i, j} (i != j) in the array such that the sum of a[i] and a[j] is greater than 0.'''

def valid_pair_sum(a: list, n: int):
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] > 0:
                count += 1
    return count

#better approach

def valid_pair_sum2(a: list, n: int):
    a.sort()

    count = 0
    l = 0
    r = n - 1

    while l < r:
        if a[l] + a[r] >= 1:
            count += r - l
            r -= 1
        else:
            l += 1

    return count

a = [3, -2, 1]
n = len(a)

print(valid_pair_sum2(a, n))