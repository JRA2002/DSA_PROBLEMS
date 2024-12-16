'''You are given an array A of size N. Let us denote S as the sum of all integers present in the array. Among all integers present in the array, find the minimum integer X such that S ≤ N*X.'''

def minimum_integer(N: int, A: list):
    S = 0
    for num in A:
        S += num
    
    mini = max(A)
    for num in A:
        if S <= N*num and num <= mini:
            mini = num
    return mini


A = [3]
N = len(A)
res = minimum_integer(N, A)
print(res)