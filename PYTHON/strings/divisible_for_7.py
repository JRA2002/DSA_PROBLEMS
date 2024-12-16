'''Given a number N, the task is to check if it is divisible by 7 or not.
Note: You are not allowed to use the modulo operator, floating point arithmetic is also not allowed'''

def divisible7(num):
    c = num // 7
    num1 = c * 7
    if num1 == num :
        return True
    return False

res = divisible7(371)
print(res)