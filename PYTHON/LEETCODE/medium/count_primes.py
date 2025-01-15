'''Given an integer n, return the number of prime numbers that are strictly less than n.'''

def count_primes(n: int):
        if n <= 2:
            return 0
        primes = 0
        
        lista = [i for i in range(n + 1)]
        lista[0] = 0
        lista[1] = 0

        for i in range(n):
            if lista[i]:
                primes += 1
                h = 2
                while i * h <= n:
                    lista[i*h] = 0
                    h += 1

        return primes

n = 10

print(count_primes(n))