'''Given an array arr[] you have to find the maximum value of abs(i – j) *min(arr[i], arr[j]) where i and j vary from 0 to n-1 and i != j. '''

def find_max_value(arr: list):
    maxi = 0
    n = len(arr)
    i = 0
    j = n - 1
    while i <= n-1 and j >= 0:
        res = abs(i-j)*min(arr[i],arr[j])
        if res > maxi:
                maxi = res
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    return maxi

arr = [-8, 4, -5, 9, -2, 10, -4, -8, 6, -1]

res = find_max_value(arr)
print(res)