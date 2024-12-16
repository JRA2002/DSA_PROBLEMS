def generate_permutations(s):
    if len(s) == 0:
        return ['']
    
    permutations = []
    
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        
        for perm in generate_permutations(remaining):
            permutations.append(char + perm)
    
    return permutations
   


a = ord('a') ^ ord('b')
print(a)