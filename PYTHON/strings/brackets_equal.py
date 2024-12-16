'''Given a string of brackets, the task is to find an index k which 
decides the number of opening brackets is equal to the number of closing brackets. '''

def equal_brackets(s):
    op = 0
    cl = 0
    for i, v in enumerate(s):
        if v == ')':
            cl += 1
        else:
            op += 1
        if cl  == op:
            return i + 1

    return op, cl

s = '((()))(('
res = equal_brackets(s)
print(res)
