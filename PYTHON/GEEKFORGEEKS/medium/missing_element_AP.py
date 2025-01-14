'''Find the missing element from an ordered array arr[], elements of array arr representing an Arithmetic Progression(AP).

Note: An element will always exist that, upon inserting into a sequence forms Arithmetic progression. Boundary elements (first and last elements) are not missing.'''

def find_missing(arr: list):
    l = 0
    r = (len(arr)) - 1
    diff = 0
    while l <= r:
        m = (l+r) // 2
        print(m)
        if (m == 0 and arr[m] + diff < arr[r]) or arr[m] - arr[m-1] > arr[m+1] - arr[m] or arr[m] - arr[m-1] < arr[m+1] - arr[m]:
            if m == 0:
                return arr[m] + diff
            elif arr[m] - arr[m-1] > arr[m+1] - arr[m]:
                return 2 * arr[m] - arr[m+1] 
            return 2 * arr[m] - arr[m-1] 
       
        elif arr[m] - (m - l)*(arr[m] - arr[m-1]) == arr[l]:
            diff = arr[m] - arr[m-1]
            l = m + 1
        else:
            diff = arr[m+1] - arr[m]
            r = m - 1

    
        
arr = [2, 4, 8, 10, 12, 14]

print(find_missing(arr))