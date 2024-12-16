'''Given a number N. Find if it can be expressed as sum of two prime numbers.'''

def primes_sum(N: int):
    def get_primes(N: int):
        primes = []
        lista = [i for i in range(N + 1)]
        print(lista)
        lista[0] = 0
        lista[1] = 0
        count = 0
        for i in range(N + 1):
            if lista[i]:
                primes.append(i)
                count += 1
                h = 2
                while i * h <= N:
                    lista[i*h] = 0
                    h += 1
        print(primes)
        return primes
    
    p = get_primes(N)
    i = 0
    j = len(p) - 1
    while i <= j:
        if p[i] + p[j] > N:
            j -= 1
        elif p[i] + p[j] == N: 
            return p[i] ,p[j]
        else:
            i += 1
    return False

# optimal solution


def is_prime(N):
    if N == 2 or N==3:
        return True
    i = 2
    while i * i <= N:
        if  N%i == 0:
            return False
        i += 1
    return True
    
def is_possible(num):
    if num < 4:
        return False
    if num % 2 == 0:
        return True
    return is_prime(num - 2)
    
def primes_sum2(N):
    if is_possible(N):
        return 'Yes'
    return 'No'
       

N = 34

res = primes_sum2(N)
print(res)