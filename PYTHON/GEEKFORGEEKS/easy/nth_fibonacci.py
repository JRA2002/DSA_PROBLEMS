'''Given a positive integer n, find the nth fibonacci number. 
Since the answer can be very large, return the answer modulo 1000000007.

Note: for the reference of this question take first fibonacci 
number to be 1'''

def nth_fibonacci(n):
   
    a = 0
    b = 1
    
    for _ in range(n):
        suma = a + b
        a, b = b, suma
    return a

# memoization
def nth_fibonacci1(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = nth_fibonacci1(n-1, memo) + nth_fibonacci1(n-2, memo)
    return memo[n]

n = 7
res = nth_fibonacci1(n)
print(res)