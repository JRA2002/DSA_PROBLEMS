'''Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return false.'''

def check_status(a, b, flag):
    if a >= 0 and flag == False:
        if b >= 0:
            return False
        else:
            return True
    elif b >= 0 and flag == False:
        if a >= 0:
            return False
        else:
            return True
    if a < 0 and b < 0 and flag == True:
        return True
    return False
    

a = 1
b = -1
flag = False

res = check_status(a, b, flag)
print(res)