'''Given a string str consisting of opening and closing parenthesis
 '(' and ')'. Find length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
Opening parenthesis must be closed in the correct order.'''

def valid_parenthesis(str1):
    stack = []
    count = 0

    for char in str1:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) > 0:
                top = stack.pop()
            else:
                top = 'a'
            if char == ')' and top == '(':
                count += 2
    
    return count


def valid_parenthesis2(str1):
    o = 0
    c = 0
    suma =  0
    for char in str1:
        if char == '(':
            o += 1
        else:
            c += 1
        if o < c:
            c = 0
        if c == o and c != 0 and o != 0:
            suma = suma + c + o
            c = 0
            o = 0
    if o >= c:
        return c+c+suma
    return suma      
    

str1 = '()()(()())))))((()))(()()))))(((()()(()()())))))))(())))'
res = valid_parenthesis(str1)
print(res)