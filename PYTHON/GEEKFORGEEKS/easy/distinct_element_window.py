'''Given an array of integers and a number k. Find the count of distinct elements in every window of size k in the array.'''

def count_distinct(k: int, arr: list):
    ans = []
    n = len(arr)
    hashmap = {}
    count = 0
    for i in range(k):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = 1
            count += 1
        else:
            hashmap[arr[i]] += 1
    print(hashmap)
    ans.append(count)
    for i in range(1, n - k + 1):
        hashmap[arr[i-1]] -= 1
        if hashmap[arr[i-1]] == 0:
            count -= 1
        if arr[i+k-1] not in hashmap or hashmap[arr[i+k-1]] == 0:
            count += 1
            hashmap[arr[i+k-1]] = 1
        else:
            hashmap[arr[i]] += 1
        ans.append(count)
        print(hashmap)
    return ans


def count_distinct2(k: int, arr: list):
    pass

k = 2
arr = [1, 1,1,1,1]

res = count_distinct(k, arr)
print(res)