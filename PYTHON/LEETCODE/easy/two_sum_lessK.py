'''Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.'''

def two_sum_less(A: list, K: int):
    res = -1
    A.sort()
    l = 0
    r = len(A) - 1

    while l < r:
        if A[l] + A[r] < K:
            res = max(res, A[l] + A[r])
            l += 1
        else:
            r -= 1

    return res

A = [3,1,2,5,4,6]
K = 12

print(two_sum_less(A, K))

#Time Complexity: O(nlogn)
# Space Complexity: S(1)