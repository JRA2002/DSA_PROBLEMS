'''Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.'''

def perect_square(num: bool):
    if num == 0 or num == 1:
         return True
    s = 1
    e = num
   
    while s <= e:
        m = (e-s)//2 + s
        if m * m == num:
            return True
        elif m * m > num:
            e = m - 1
        else:
            s = m + 1 
    return False

num = 18
res = perect_square(num)

print(res)