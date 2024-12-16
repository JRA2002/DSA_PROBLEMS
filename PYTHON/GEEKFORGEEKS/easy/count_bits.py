'''Given a positive integer n. Your task is to return the count of set bits.'''

def count_bits(n):
    count = 0
    while n != 0:
        res = n%2
        if res == 1:
            count += 1
        n = n//2
    return count
n = 8
res = count_bits(n)
print(res)