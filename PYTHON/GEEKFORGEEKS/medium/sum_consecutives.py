'''Given a number N, the task is find the number of ways to represent this number as a sum of 2 or more consecutive natural numbers.'''
# optimal approach
def get_count(N):
    L = 1
    count = 0
    # N = a + (a+1) + (a+2) + ... + (a+L)
    # clearing 'a'
    # a = (N - L*(L+1)/2)/ (L + 1)
    # asuming N > L*(L+1)/2)
    while (L*(L+1)) < 2*N:
        a = (1.0*N - L*(L+1)/2)/ (L + 1)
        if a - int(a) == 0:
            count += 1
        L += 1
    return count

N = 15
res = get_count(N)
print(res)