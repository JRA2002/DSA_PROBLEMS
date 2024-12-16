def quicksort(arr, left, right):
    if left < right:
        partition_pos = position(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def position(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while arr[i] < pivot and i < right:
            i += 1
        while arr[j] >= pivot and j > left:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        
    return i

arr = [4,7,1,2,9,3,10]
right = len(arr) - 1
quicksort(arr, 0, right)
print(arr)




    

    
