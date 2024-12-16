'''Given an array arr[] of integers. Find an element such 
that all the elements to its left are smaller and to its 
right are greater. Print -1 if no such element exists.

Note:  There can be more than one such element. In that 
case, print the first such number occurring in the array.'''

def find_element(arr):
    
    for i in range(0, len(arr)):
        right = True
        left = True
        # right side
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                print(arr[i], arr[j])
                right = False
                break
        # left side
        if right:
            for j in range(i-1, -1,-1):
                if arr[i] < arr[j]:
                    print(arr[i], arr[j])
                    left = False
                    break
        if right and left:
            return arr[i]
    return -1
        
arr = [15843 ,6965 ,18610,13008,5097 ,27826]
res = find_element(arr)
print(res)