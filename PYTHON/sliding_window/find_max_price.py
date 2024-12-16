'''find the maximun price in an array with lenght == n
in a group of 'k' elements'''

def max_price(arr, k):
    if len(arr) < k:
        return 0
    total = sum(arr[:k])
    maximun = total
    for i in range(len(arr) - k):
        total -= arr[i]
        total += arr[k+i]
        maximun = max(total, maximun)
    return maximun

'''find the minimum price in an array with lenght == n
in a group of 'k' elements'''

def min_price(arr, k):
    if len(arr) < k:
        return 0
    total = sum(arr[:k])
    minimun = total
    for i in range(len(arr) - k):
        total -= arr[i]
        total += arr[k+i]
        minimun = min(minimun, total)
    return minimun


arr = [1,2,3,4,5,6,7]
maxi = max_price(arr, 3)
mini = min_price(arr, 3)
print(maxi)
print(mini)