'''Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. '''

def count_freq(arr: list, target: int):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l+r) // 2
        if arr[m] == target:
            tmp = m
            countL = 0
            while m >= 0 and arr[m] == target:
                countL += 1
                m -= 1
            countR = 0
            while tmp < len(arr) and arr[tmp] == target:
                countR += 1
                tmp += 1

            return countL + countR - 1
        
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1

    return 0
                




arr = [8, 9, 10, 12, 12, 12]
target = 12

print(count_freq(arr, target))
