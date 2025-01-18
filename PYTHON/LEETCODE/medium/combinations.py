'''Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.'''

def combinations(n: int, k: int):
   
    ans = []
    aux = []

    def backtrack(m):
        if k == len(aux):
            ans.append(aux[:])
            return
        
        for num in range(m, n + 1):
          
                aux.append(num)
                backtrack(num+1)
                aux.pop()
                
    backtrack(1)

    return ans
            

n = 4
k = 2

print(combinations(n, k))