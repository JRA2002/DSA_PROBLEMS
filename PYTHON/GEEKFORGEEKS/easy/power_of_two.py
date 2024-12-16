'''Given a non-negative integer n. The task is to check if it is a power of 2. '''

def is_power_two(n):
       
        res = 0
        while n > 0:
            res = n%2
            if res > 0:
                return False
            n = n//2
            if n == 1:
                return True

res = is_power_two(2561212412)
print(res)
