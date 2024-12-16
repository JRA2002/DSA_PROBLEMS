'''Find the majority element in the array. A majority 
element in an array A[] of size n is an element that 
appears more than n/2 times (and hence there is at most one such element). '''

def majority(arr: list):
    set1 = set(arr)
    media = len(arr) / 2
    for i in set1:
        a = arr.count(i)
        if a > media:
            return i
    return None

arr =  [3, 3, 4, 2, 4, 4, 2, 4]
res = majority(arr)
print(res)

# Time Complexity:O(M*N)
# Auxiliary Space: O(M)
