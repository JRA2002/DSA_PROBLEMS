'''Given a sorted array arr[] of size n without duplicates, and given a 
value x. Floor of x is defined as the largest element k in arr[] such
 that k is smaller than or equal to x. Find the index of k(0-based indexing).'''

def find_floor(A, N, X):
    i = 0
    j = N - 1
    while i <= j:
        midd = (i+j)//2
        if A[midd] > X:
            j = midd - 1
        elif A[midd] == X:
            return midd
        else:
            i = midd + 1
    if A[midd] > X:
        return midd - 1
    elif A[midd] < X:
        return midd

X = 0
A = [1,2,8,10,11,12,19]
N = len(A)

res = find_floor(A, N, X)
print(res)