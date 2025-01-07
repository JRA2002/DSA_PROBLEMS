'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

def valid_parenthesis(s: str):
    stack = []
    mapa = {')':'(', ']':'[', '}':'{'}

    for c in s:
        if c != ')' and c != ']' and c != '}':
            stack.append(c)
        else:
            if len(stack) != 0:
                temp = stack.pop()
            else:
                temp = ''
            if temp != mapa[c]:
                return False

    if len(stack) == 0:
        return True
    return False
    
s = ")"

print(valid_parenthesis(s))