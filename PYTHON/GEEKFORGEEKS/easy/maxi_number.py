'''Given a number N, write a program to find a maximum number that can be formed using all of the digits of this number.
Note: The given number can be very large, so the input is taken as a String.'''

def find_maximum(N):
    lista = [i for i in N]
    lista.sort(reverse=True)
    new = ''
    for i in lista:
        new += i
    return new

N = "38293367"
res = find_maximum(N)
print(res)