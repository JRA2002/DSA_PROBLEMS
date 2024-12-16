'''You are given a 0-indexed, strictly increasing integer array
 nums and a positive integer diff. A triplet (i, j, k) is an 
 arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.'''

def arithmetic_triplets(arr, diff):
    count = 0
    for i in range(0,len(arr) - 1):
        j = i + 1
        k = len(arr) - 1
        while i < j and j < k :
            if arr[k] - arr[j] == diff and arr[j] - arr[i] == diff:
                count += 1
                break
            elif arr[j] - arr[i] == diff:
                k -= 1
            else:
                j += 1
    return count


arr = [0,1,4,6,7,10]
diff = 3
res = arithmetic_triplets(arr, diff)
print(res)

# Time Complexity:O(N^2)
# Auxiliary Space: O(1)

a = 'a'
if isinstance(a, int):
    print('kello')