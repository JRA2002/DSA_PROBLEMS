'''You are given two arrays arr1 and arr2. The task is to find the minimum value of arr1[0] * arr2[0] + arr1[1] * arr2[1] + .... + arr1[N-1] * arr2[N-1], where the shuffling of elements of arrays arr1 and arr2 is allowed.'''

def min_sum_product(arr1, arr2):

    arr1.sort(reverse=True)
    arr2.sort()
    ans = 0
    for i in range(len(arr1)):
        ans += arr1[i] * arr2[i]
    return ans

arr1 = [3, 1, 1] 
arr2 = [6, 5, 4]

res = min_sum_product(arr1, arr2)
print(res)
