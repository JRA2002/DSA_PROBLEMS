'''Given an array arr[] of length N, find the length of the longest sub-array with a sum equal to 0.'''

# we solve this problem using hash map where O(N) and S(N),but using iterative 
# for every subarray the time complexity is 0(N**2) and space use is S(N), 
# THATS BAAAD !!
def max_length(arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == 0:
            max_len = i + 1

        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i

    return max_len, hash_map

arr = [15, -2, 2, -8, 1, 7, 10, 13]
res = max_length(arr)

print(res)


