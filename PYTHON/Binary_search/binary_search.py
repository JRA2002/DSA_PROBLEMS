def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        midd = (left + right) // 2
        if arr[midd] == target:
            i = midd
            j = midd
            count = 1
            while target == arr[i+1]:
                count += 1
                i += 1
            while target == arr[j-1]:
                count += 1
                j -= 1

            return count
        elif arr[midd] < target:
            left = midd + 1
        else:
            right = midd - 1
    return -1




# using recursion to find binary search
def find_midd(min, max):
    midd = (min + max) // 2
    return midd

def recursion_binary(target, arr, min, max):
    if max < min :
        return -1
    else:
        midd = find_midd(min, max)

        if arr[midd] < target:
            recursion_binary(target, arr, midd + 1, max)
        elif arr[midd] > target:
            recursion_binary(target, arr, min, midd - 1)
        else:
            return midd
        