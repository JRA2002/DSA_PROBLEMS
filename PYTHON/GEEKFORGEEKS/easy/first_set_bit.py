'''Given an integer N. The task is to return the position 
of first set bit found from the right side in the binary 
representation of the number.
Note: If there is no set bit in the integer N, then 
return 0 from the function.  '''

def set_first_bit(n):
    i = 1

    while n > 0:
        res = n % 2
        if res == 1:
            return i
        i += 1
        n = n // 2
    return 0
n = 12
res = set_first_bit(n)
print(res)