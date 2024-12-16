'''Given a permutation of the first n natural numbers in an array arr[], determine if the array can be sorted in exactly two swaps. A swap can involve the same pair of indices twice.

Return true if it is possible to sort the array with exactly two swaps, otherwise return false.'''

def check_sorted(N, A):
   
    swap = 0
    for _ in range(2):
        i = 0
        j = N - 1
        while i <= j:
            print(A[i],A[j])
            if A[i] != i+1 and A[j] != j+1 :
                A[i], A[j] = A[j], A[i]
                swap += 1
                i += 1
                j -= 1
            elif A[i] == i+1:
                i += 1
            else:
                j -= 1

            if swap > 2:
                return False
            
    for i in range(N-1):
        if A[i] > A[i+1]:
            return False
        
    return True


A = [7 ,1, 3, 4, 5, 6, 2]
N = len(A)

res = check_sorted(N, A)
print(res)