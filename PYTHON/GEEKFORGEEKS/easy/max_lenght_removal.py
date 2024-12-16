'''You are given a binary string S consisting of only characters '0' and '1'.
 You can repeatedly delete any occurrence of the sub-string "100" from S. 
 Your task is to determine the length of the longest continuous sub-string 
 that can be completely removed by applying this deletion operation.'''

def max_lenght(s: str):
    stack = []
    stack.append(['@',-1])
    maxi = 0

    for i in range(len(s)):
        stack.append([s[i], i])

        while (len(stack) >= 3 and 
            stack[len(stack) - 3][0] == '1' and 
            stack[len(stack) - 2][0] == '0' and
            stack[len(stack) - 1][0] == '0'
            ):

            stack.pop()
            stack.pop()
            stack.pop()

        temp = stack[-1]
        maxi = max(maxi, i - temp[1])
        
    return maxi
        



s = "1001100"
res = max_lenght(s)
print(res)