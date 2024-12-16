'''You start with an array A of size N. Initially all elements of the array A are zero. You will be given K positive integers. Let j be one of these integers, you have to add 1 to all A[i], where i ≥ j. Your task is to print the array A after all these K updates are done.

Note: Indices in updates array are given in 1-based indexing. That is updates[i] are in range [1,N].'''

def adding_ones(a, n, updates, k):
    m = 0
    while m <= k - 1:
        j = updates[m]
        for i in range(n):
            im = i + 1
            if im >= j:
                a[i] = a[i]+1
        m += 1
    return a

# optimal approach

def adding_ones2(a, n, updates, k):
    pass

a = [0, 0]
updates = [1, 1, 1]
k = 3

print(adding_ones2(a, len(a), updates, k))