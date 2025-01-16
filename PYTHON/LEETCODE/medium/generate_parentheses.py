'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''

def generate_parentheses(n: int):
    res = []
    stack = []
    def backtrack(op, cl):
       
        '''
        Recursive function to backtrack and build all well-formed parentheses
        
        Parameters:
        op (int): the number of open parentheses
        cl (int): the number of close parentheses
        
        Returns:
        res 
        '''

        if op == cl and op == n:
            res.append("".join(stack))
            return

        if n > op:
            stack.append('(')
            backtrack(op + 1, cl)
            stack.pop()
          
        if op > cl:
            stack.append(')')
            backtrack(op, cl + 1)
            stack.pop()
          

    backtrack(0, 0)

    return res

n = 3
res = generate_parentheses(n)
print(res)
