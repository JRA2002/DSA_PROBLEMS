'''Given an array arr of positive integers and another number target.
 Determine whether two elements exist in arr whose sum is exactly 
 target or not. Return a boolean value true if two elements exist in arr else return false.'''

def two_sum(arr: list, target):
    arr.sort()
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] > target:
            j -= 1
        elif arr[i] + arr[j] == target:
            return True
        else:
            i += 1
    return  False

# optimal approach

def two_sum2(arr: list, target):
    mapa = {}
    for i in range(len(arr)):
        if target - arr[i] not in mapa:
            mapa[arr[i]] = i
        else:
            return True
        
    return False

arr = [1,8,2,6,5]
target = 27

res = two_sum2(arr, target)
print(res)