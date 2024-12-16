'''Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".'''

def parenthesis_checker(str1):
    stack = []

    for char in str1:
        if char in '[({':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (char == ']' and top != '[') or (char == '}' and top != '{') or (char == ')' and top != '('):
                return False
    if len(stack) > 0:
        return False
    return True

str1 = '{[]}([]'
res = parenthesis_checker(str1)
print(res)