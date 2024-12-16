'''Find the largest pair sum in an array of distinct integers.'''

def largest_pair_sum(arr: list):
    maxi = 0
    for num in arr:
        if num > maxi:
            maxi = num
    maxi2 = 0
    for num in arr:
        if num > maxi2 and num != maxi:
            maxi2 = num
    return maxi+maxi2


arr = [12, 34, 10, 6, 40]
res = largest_pair_sum(arr)
print(res)