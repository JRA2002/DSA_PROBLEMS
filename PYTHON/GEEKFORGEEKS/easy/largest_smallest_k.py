'''Given a sorted array arr[] of size n without duplicates, 
and given a value x. Floor of x is defined as the largest 
element k in arr[] such that k is smaller than or equal to x. 
Find the index of k(0-based indexing).'''

def largest_smaller(A, N, X):
    i = 0
    j = N - 1

    while i <= j:
        midd = (i+j)//2
        if A[midd] > X:
            j -= 1
        elif A[midd] == X:
            if midd == 0:
                 return -1
            return midd-1
        else:
            i += 1
    
    if midd == 0:
            return -1
    elif A[midd] < X:
        return midd
    else:
        return midd-1


A = [2,8,10,11,12,19]
N = len(A)
X = 32

res = largest_smaller(A, N, X)
print(res)