'''Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.'''

def count_digits(n: int):
    count = 0
    temp = n

    while temp > 0:
        r = temp % 10
        if r != 0 and n % r == 0:
            count += 1

        temp = temp // 10
 

    return count



n = 12

print(count_digits(n))