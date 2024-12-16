''''Given an array arr[]  of integers that might contain duplicates, find the element whose last appearance is earliest.'''

def last_seen_element(arr: list):
    dict1 = {}
    mini = len(arr)
    for i in range(len(arr)-1, -1, -1):
        if arr[i] not in dict1:
            dict1[arr[i]] = i
            if i <= mini:
                mini = i
    return arr[mini]

    


arr = [10, 20, 30, 40, 10]

res = last_seen_element(arr)
print(res)