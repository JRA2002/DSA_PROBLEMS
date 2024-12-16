'''Given a number N, check if a number is perfect or not. 
A number is said to be perfect if sum of all its factors 
excluding the number itself is equal to the number. 
Return 1 if the number is Perfect otherwise return 0.'''

def is_perfect(N):
    suma = 0

    for i in range(1, N):
        if N%i == 0:
            suma += i
    if suma == N:
        return 1
    return 0

#optimal approach
def is_perfect1(N):
    suma = 1
    i = 2
    while i * i < N:
        if N%i == 0:
            if i == N//i:
                suma += i
            else:
                suma += i
                suma += N//i
        i += 1
    if suma == N:
        return 1
    return 0


N = 6
res = is_perfect1((N))
print((res))
