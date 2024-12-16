'''You will be given an array A of N non-negative integers. Your task is to find the
rightmost non-zero digit in the product of array elements.'''


def rightmost_non_zero(N, A):
    prod = 1
    for num in A:
        prod *= num
        if prod == 0:
            return -1
        
    str1 = str(prod)
    lista = [int(i) for i in str1]


def rightmost_non_zero1(N, A):
    p = 1
    for num in A:
        p *= num
        if p == 0:
            return -1
        elif p%10 == 0:
            p = p//10
    if p%10 == 0:
       
        return p
    return p

#optimal approach
def rightmost_non_zero3(N, A):
        # To store the count of times 5 can 
        # divide the array elements 
        c5 = 0 
        # Divide the array elements by 5 
        # as much as possible 
        for i in range(N):
            while (A[i] > 0 and A[i] % 5 == 0):
                A[i] //= 5 
                # increase count of 5 
                c5 += 1 
      
        # Divide the array elements by 
        # 2 as much as possible 
        for i in range(N):
            while (c5 and A[i] > 0 and (A[i] % 2 == 0)):
                A[i] //= 2
      
                # Decrease count of 5, because a '2' and 
                # a '5' makes a number with last digit '0' 
                c5 -= 1 
                
        ans = 1
        for i in range(N):
            ans = (ans * A[i] % 10) % 10
      
        # If c5 is more than the multiplier 
        # should be taken as 5 
        print(c5)
        print(ans)
        if c5: 
            ans = (ans * 5) % 10
            
        if ans: 
            return ans 
      
        return -1

A = [3,23,30,45]
N = len(A)
res = rightmost_non_zero3(N, A)
print(res)