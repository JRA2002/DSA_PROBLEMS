'''Given a positive integer N., The task is to find the value 
of Σi from 1 to N F(i) where function F(i) for the number i is 
defined as the sum of all divisors of i.'''

def sum_divisors(N):
    def find_suma(N):
        suma = 0
        i = 1
        while (i**2) <= N:
            if N%i == 0:
                suma += i
                res = N // i
                if N%res == 0 and res != i:
                    suma += res
            i += 1
        return suma
    
    res = 0
    for i in range(1,N+1):
        res += find_suma(i)
    return res

# optimal approach

def sum_divisors2(N):
    suma = 0
    for i in range(1, N+1):
        res = N//i
        suma += i*res
    return suma

    
N = 500000
res = sum_divisors2(N)
print(res)