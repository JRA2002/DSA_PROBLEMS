'''Given a sorted (in ascending order) and rotated array arr of distinct elements which may be rotated at some point and given an element key, the task is to find the index of the given element key in the array arr. The whole array arr is given as the range to search.

Rotation shifts elements of the array by a certain number of positions, with elements that fall off one end reappearing at the other end.

Note:- 0-based indexing is followed & returns -1 if the key is not present.'''

def search_index(arr, key):
        idx = arr[0]
        n = len(arr)
        for i in range(n - 1,-1,-1):
            if arr[i] >= idx:
                idx = i
                break
       
        if key >= arr[0]: 
            i = 0
            j = idx  
        else:
            i = idx + 1
            j = n - 1
        while i <= j:
            midd = (i+j)//2
    
            if arr[midd] == key :
                return midd
            elif arr[midd] < key:
                i = midd + 1
            else:
                j = midd - 1
            
        return -1

arr = [7,1,2,3,4,5,6]
key = 2

res = search_index(arr, key)
print(res)

# Time Complexity: O(log(N))
# Auxiliary Space: O(1)