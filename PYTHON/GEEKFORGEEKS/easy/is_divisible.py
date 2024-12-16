'''Given a number in its binary form find if the given binary 
number is a multiple of 3. It is recommended to finish the task 
using one traversal of input binary number.'''

def is_divisible(s):
    num = int(s, 2)
    if num % 3 == 0:
        return 1
    return 0
s = '0011'

res = is_divisible(s)
print(res)