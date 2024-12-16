
def harmonic_sum(n):
    
    suma =  (2*n - 3)/(n - 2) * (n - 1) + 1/n + 1

    return suma

res = harmonic_sum(5)
print(res)