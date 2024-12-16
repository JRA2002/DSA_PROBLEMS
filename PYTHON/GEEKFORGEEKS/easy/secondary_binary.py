'''Given two numbers A and B count all the number between the given range 
whose second least significant digit in the binary representation of the number is 1.'''
#optimal approach
def find_digit1(A, B):

    ans = 0

    if A%4 == 1:
        A += 3
        ans += 2
    elif A%4 == 2:
        A += 2
        ans += 2
    elif A%4 == 3:
        A += 1
        ans += 1
    
    if B%4 == 2:
        B -= 2
        ans += 1
    elif B%4 == 3:
        B -= 3
        ans += 2
    
    ans += ((B-A)//4) * 2
    return ans
         
         
def find_digit2(A, B):
        
        count = 0
        cos = (A//4) - 2
        while 2+4*cos <= B:
            num1 = 2+4*cos
            num2 = num1 + 1
            
            if num1 >= A and num1 <= B :
                count += 1
            if num2 >= A and num2 <= B:
                count += 1
            cos += 1
        return count

A = 13
B = 45
res = find_digit1(A, B)
print(res)