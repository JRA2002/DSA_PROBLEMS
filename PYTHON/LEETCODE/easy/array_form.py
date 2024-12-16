'''The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.'''

def array_form(num, k):
    suma = 0
    n = len(num) - 1
    for i in range(len(num)):
        suma += num[i]*(10**n)
        n -= 1
    suma = suma + k
    res = [] 
    
    i = 0
    while suma > 0:
        num = suma % 10
        res.insert(0,num)
        suma = suma // 10
    return res

# optimal approach
def array_form2(num, k):
    
    for i in range(len(num)-1,-1,-1):
        k, num[i] = divmod(num[i]+k,10)
    print(k) 
    while k:
            k, a = divmod(k, 10)
            num = [a] + num
            print(num)
    return num

num = [0]
k = 1000

res = array_form2(num, k)
print(res)
