'''You are given 2 numbers (n , m); the task is to find n√m (nth root of m).'''
import math
def nth_root(n, m):

    res = round(m**(1/n), 2)
    res1 = math.pow(res, n)
    
    if m == res1:
        return round(res)
    else:
        return -1
    

n = 2
m = 9

res = nth_root(n, m)
print(res)