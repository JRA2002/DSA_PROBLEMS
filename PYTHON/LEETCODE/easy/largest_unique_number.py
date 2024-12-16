'''Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.'''

def unique_number(A: list):
    hmap = {}
    for num in A:
        if num not in hmap:
            hmap[num] = 1
        else:
            hmap[num] += 1

    maxi = -1
    for k,v in hmap.items():
        if v == 1 and k > maxi:
            maxi = k

    return maxi
    

A = [51,51]

res = unique_number(A)
print(res)