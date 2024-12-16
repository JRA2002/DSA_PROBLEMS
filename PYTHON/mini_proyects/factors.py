def factors(n): 
    k = 1
    while k * k < n: 
        if n % k == 0:
            yield k
            k += 1
        else:
           yield k-k
            
          
   
def numbers(n):
    k = 1
    while k < n:
        yield k
        k += 1

for num in factors(10):
    print(num)