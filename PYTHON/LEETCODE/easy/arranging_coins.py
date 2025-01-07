'''You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.'''

def arrange_coins(n: int):

    l = 1
    r = n
    while l <= r:
        m = (l+r) // 2
        gauss = m * (m+1)//2
        if gauss > n:
            r = m - 1
        else:
            l = m + 1

    return r
        



n = 8
print(arrange_coins(n))