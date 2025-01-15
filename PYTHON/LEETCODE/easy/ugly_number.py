'''An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.'''

def is_ugly(n: int):
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0:
            n = n // 3
        elif n % 5 == 0:
            n = n // 5
        else:
            return False
        
        if n == 1:
            return True
        
    return False
        
        



n = 168

print(is_ugly(n))