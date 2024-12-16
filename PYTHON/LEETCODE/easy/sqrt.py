'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.'''

def mysqrt(x):
        i = 1
        while i * i <= x:
            i += 1
        return i - 1


# optimal approach

def mysqrt2(x):
    if x == 0 or x == 1:
         return x
    s = 1
    e = x
   
    while s <= e:
        m = (e-s)//2 + s
        if m * m == x:
            return m
        elif m * m > x:
            e = m - 1
        else:
            s = m + 1 
    return e
x = 8
res = mysqrt2(x)
print(res)