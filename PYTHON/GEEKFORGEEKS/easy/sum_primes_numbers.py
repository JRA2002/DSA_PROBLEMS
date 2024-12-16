'''You are given a positive integer N, return the sum of all 
prime numbers between 1 and N(inclusive).'''

def find_sum_primes(n):
    #criba erastostenes

    primes = []
    lista = [i for i in range(n + 1)]
    print(lista)
    lista[0] = 0
    lista[1] = 0
    print(lista)
    count = 0
    for i in range(n + 1):
        if lista[i]:
            print(lista[i])
            primes.append(i)
            count += 1
            h = 2
            while i * h <= n:
               
                lista[i*h] = 0
                h += 1
    print(primes)
    

n = 50
res = find_sum_primes(n)
print(res)