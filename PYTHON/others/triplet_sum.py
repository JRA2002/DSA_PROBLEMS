'''Given an array arr[] of size n and an integer sum. 
Find if there’s a triplet in the array which sums up to the given integer sum.'''

def triplet_sum(arr, suma):
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] > suma:
            i += 1

        if arr[j] > suma:
            j -= 1

        if arr[i] + arr[j] < suma:
            diff = suma - (arr[i] + arr[j])
            if diff in arr:
                return True
            i += 1
        else:
            if arr[i] < arr[j]: 
                i += 1
            else:
                j -= 1
        
    return False

    
        
arr = [2, 4, 45, 6, 10, 8]
res = triplet_sum(arr, 13)
print(res)
# Time complexity: O(N) 
# Auxiliary Space: O(1)