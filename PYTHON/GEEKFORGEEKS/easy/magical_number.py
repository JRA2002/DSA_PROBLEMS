'''Your friend loves magic and he has coined a new term - "Magical number". To perform his magic, he needs that magic number. You are given a sorted array arr of distinct integers. A number arr[i] is a magical number if arr[i] = i (0-based indexing).
You have to return the leftmost magical number present in the given array arr, if there is no magical number in the array arr then return -1'''

def magical_number(arr: list):
    i = 0
    j = len(arr) - 1
    ans = []
    count = 0
    while i <= j:
        midd = (i+j)//2
        if arr[midd] == midd:
            ans.append(midd)
            count += 1
            j = midd - 1
        elif arr[midd] > midd:
            j = midd - 1
        else:
            i = midd + 1
    if count == 0:
        return -1
    return ans[-1]

arr = [-1, 1, 2, 3, 5, 7]

res = magical_number(arr)
print(res)