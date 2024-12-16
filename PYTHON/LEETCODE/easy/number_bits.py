'''Given a positive integer n, write a function that returns the number of 
set bits
 in its binary representation (also known as the Hamming weight).'''

def number_bits(n: int):
    count = 0
    while n != 0:
        r = n%2
        if r == 1:
            count += 1
        n = n // 2

    return count

n = 2147483645

print(number_bits(n))