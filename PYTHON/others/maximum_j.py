'''Given an array arr[] of N positive integers. The task is to 
find the maximum of j – i subjected to the constraint of arr[i] <= arr[j].'''
def maximum_index(arr: list):

    j = len(arr) - 1
    i = 0
    maxi = 0

    while j > 0:
        if arr[i] <= arr[j]:
            res =  j - i
            if res > maxi:
                maxi = res
        j -= 1
    j = len(arr) - 1
    i = 0
    while i < j:
        if arr[i] <= arr[j]:
            res =  j - i
            if res > maxi:
                maxi = res
        i += 1
    j = len(arr) - 1
    i = 0
   
    while i < j:
        if arr[i] <= arr[j]:
            res = j - i
            if res > maxi:
                maxi = res
        i += 1
        j -= 1
    
    return maxi

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
res = maximum_index(arr)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(1)
