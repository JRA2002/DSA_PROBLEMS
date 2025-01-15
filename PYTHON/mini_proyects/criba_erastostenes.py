def find_primes(n):

    primes = []

    lista = [i for i in range(n)]
    lista[0] = 0
    lista[1] = 0

    for i in range(n + 1):
        if lista[i]:
            primes.append(i)
            h = 2
            while i * h <= n:
                lista[i*h] = 0
                h += 1

    return primes


n = 10
print(find_primes(n))

