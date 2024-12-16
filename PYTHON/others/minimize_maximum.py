'''Given the heights of N towers and a value of K, Either 
increase or decrease the height of every tower by K (only once) 
where K > 0. After modifications, the task is to minimize the 
difference between the heights of the longest and the shortest 
tower and output its difference.'''

def minimize(arr: list, k):
    arr.sort()
    diff = (arr[-1] - k) - (arr[0] + k) 
    return diff

arr = [1, 5, 15, 10]
res = minimize(arr, 3)
print(res)