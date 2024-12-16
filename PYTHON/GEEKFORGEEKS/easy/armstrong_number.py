'''You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes
 of its digits is equal to the number itself. 371 is an Armstrong number 
 since 33 + 73 + 13 = 371. 

Note: Return "true" if it is an Armstrong number else return "false".'''

def armstrong_number(n):
    res = 0
    m = n
    while n != 0:
        digit = n % 10
        res += digit**3
        print(res)
        n = n // 10
    if res == m:
        return True
    return False

n = 153
res = armstrong_number(n)
print(res)