'''Given two numbers M and N. The task is to find the
 position of the rightmost different bit in the binary 
 representation of numbers. If both M and N are the 
 same then return -1 in this case.'''

def rightmost_bit(m, n):
        if m == n:
            return -1
        i = 1
        while n >= 0 and m >= 0:
            res1 = m % 2
            res2 = n % 2
            print(res1,res2)
            if res1 != res2:
                return i
            i += 1
            n = n // 2
            m = m // 2
        return -1

m = 11
n = 11
res = rightmost_bit(m, n)
print(res)