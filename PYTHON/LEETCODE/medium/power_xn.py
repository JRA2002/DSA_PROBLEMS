'''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).'''

def mypow(x, n):
    res = 1
    res = x ** n
    return res


# optimal approach:
# using binary representation

def mypow2(x, n):
    if n < 0:
        x = 1/x
        n = abs(n)
    res = 1
    while n:
        if (n&1) != 0 :  #just when n is odd equivalnet to n%2 == !0
            res *= x  
        x *= x
        n = n >> 1  #equivalent to n = n//2
    return res

x = 2
n = -2
res = mypow2(x, n)
print(res)