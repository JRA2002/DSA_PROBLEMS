'''Given an integer x, return true if x is a 
palindrome
, and false otherwise.'''

def is_palindrome(x: int):
    if x < 0:
        return False
    ans = 0
    digits = []
    temp = x
    while x > 0:
        res = x % 10
        digits.append(res)
        x = x // 10

    expo = len(digits) - 1
    for num in digits:
        ans += num * (10**expo)
        expo -= 1
    
    return ans == temp

x = 121

print(is_palindrome(x))