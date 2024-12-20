'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.'''

def length_word(s: str):
    def isalpha(c: str):
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z')
    count = 0
    n = len(s)
    
    while not isalpha(s[n-1]):
        n -= 1

    if count == 0:
        while n > 0 and isalpha(s[n-1]):
            count += 1   
            n -= 1        
        
    return count

s = "aasd  asdfe  "
print(length_word(s))
