def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # recursion
    merge_sort(left_arr)
    merge_sort(right_arr)

    # merge
    i = 0
    j = 0
    k = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    # in case left array have single element
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    # in case right array have single element
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return arr


