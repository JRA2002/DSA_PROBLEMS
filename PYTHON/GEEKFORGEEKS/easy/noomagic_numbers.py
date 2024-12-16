'''Given two function, one is h(x) which is the product of all the 
number in an array A[ ] having size N and another
function f(x) which denotes the GCD of all the numbers in an array. 
Your task is to find the value of  h(x)f(x).
Note: Since the answer can be very large, use modulo 109+7.'''
def gcd(N,arr):
    maxi = max(arr)//2
    count = 0
    if len(arr) == 1:
        return arr[0]
    for i in range(1,maxi+1):
        for num in arr:
            if num%i == 0:
                count += 1
        if count == N:
            res = i
        count = 0
    return res

def find_value(N, A):
    h = 1
    for num in A:
        h *= num
    print(h)
    f = gcd(N,A)
    print(f)
    return (h ** f) % ((10**9)+7)
    

A = [2]
N = len(A)

res1 = find_value(N, A)
print(res1)