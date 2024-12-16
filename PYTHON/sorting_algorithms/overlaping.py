'''An interval is represented as a combination of start time and end time. 
Given a set of intervals, check if any two intervals intersect. '''

def overlaping(arr: list):
    arr.sort()
    
    a = arr[0][1] - arr[0][0]
    if a in arr[1]:
        return True, arr
    return False, arr
arr = [[1, 3], [5, 7], [2, 4], [6, 8]]
res = overlaping(arr)
print(res)