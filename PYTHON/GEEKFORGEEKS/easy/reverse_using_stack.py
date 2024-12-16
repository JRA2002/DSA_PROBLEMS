'''You are given a string S, the task is to reverse the string using stack.'''

def reverse(S):
    stack = []
    new = ''
    for i in S:
        stack.append(i)
    while len(stack) > 0:
        new += stack.pop()
    return new

S = 'GeeksforGeeks'
res = reverse(S)
print(res)