'''Given an array of integers and a number k. Find the count of distinct elements in every window of size k in the array.'''

def count_distinct(arr: list, k: int):
    ans = []
    mapa = {}
    
    for i in range(k):
        if arr[i] not in mapa:
            mapa[arr[i]] = 1
        else:
            mapa[arr[i]] += 1
    ans.append(len(mapa))

    for i in range(1, len(arr) - k + 1):
        mapa[arr[i-1]] -= 1
        if mapa[arr[i-1]] == 0:
            del mapa[arr[i-1]]
        if arr[i+k-1] not in mapa:
            mapa[arr[i+k-1]] = 1
        else:
            mapa[arr[i+k-1]] += 1
       
        ans.append(len(mapa))
    a = "as"
    a.l

    return ans



arr = [8, 10, 6]
k = 1

print(count_distinct(arr, k))