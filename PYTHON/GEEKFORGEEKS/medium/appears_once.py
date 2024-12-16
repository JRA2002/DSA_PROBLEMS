'''Given a sorted array arr[] of n positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once.'''

def search_element(arr, n):
    i = 0 
    j = n - 1
    if n == 1:
        return arr[0]
    while i <= j:
        if arr[i] == arr[i+1] and arr[j] == arr[j-1]:
            i += 2
            j -= 2
        elif arr[i] == arr[i+1] and arr[j] != arr[j-1]:
            return arr[j]
        else:
            return arr[i]


arr = [1, 1, 2, 2, 5,5,6,7,7]
n = len(arr)

res = search_element(arr, n)
print(res)