'''Given a number N. Find the length of the longest consecutive 1s in its binary'''

def max_cons_ones(N):
    count = 0
    maxi = 0
    while N != 0:
        res = N%2
        
        if res == 1:
            count += 1
        elif res == 0:
            count = 0
        if count >= maxi:
            maxi = count
        N = N//2
    return maxi

N = 14
res = max_cons_ones(N)
print(res)