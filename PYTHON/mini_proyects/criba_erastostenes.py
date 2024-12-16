def find_primes(n):

    primes = []
    lista = [i for i in range(n + 1)]

    lista[0] = 0
    lista[1] = 0
    count = 0
    for i in range(n + 1):
        if lista[i]:
            primes.append(i)
            count += 1
            h = 2
            while i * h <= n:
                lista[i*h] = 0
                h += 1
    print(primes)
    return sum(primes)


n = 5
res = find_primes(n)
print(res)

