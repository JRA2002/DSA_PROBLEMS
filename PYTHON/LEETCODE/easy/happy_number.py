'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.'''

def is_happy(n: int):
    def sum_digits(num):
        ans = 0
        while num > 0:  
            r = num % 10
            ans += r ** 2
            num = num // 10

        return ans

    mapa = {}
    while n not in mapa:
        if n == 1:
            return True
        else:
            mapa[n] = 1
            n = sum_digits(n)

    return False


n = 7

print(is_happy(n))