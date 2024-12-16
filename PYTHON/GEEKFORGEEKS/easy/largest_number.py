'''Given two numbers 'N' and 'S' , find the largest 
number that can be formed with 'N' digits and whose 
sum of digits should be equals to 'S'. Return -1 if 
it is not possible.'''

def largest_number(N, S):
    
    ed = 10 ** (N-1)
    st = 10 ** N
    for num in range(st-1,ed+1,-1):
        suma = 0
        back = num
        
        while num != 0:
            res = num%10
            suma += res
            num = num // 10
          
        if suma == S:
            return back
    return -1

# optimal approach
def largest_number2(N, S):
   
    num = 9
    res = ''
    if N > 1 and S == 0:
        return -1
    for _ in range(N):
        if num < S:
            res += str(num)
            S = S - num
        else:
            res += str(S)
            S = 0
    if S > 0:
        return -1
    return res

N = 2
S = 9

res = largest_number2(N, S)
print(res)