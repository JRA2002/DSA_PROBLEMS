'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.'''

def isomorphic(s: str, t: str):
    if len(set(s)) != len(set(t)):
        return False
    mapaS = {}
   
    i = 0
    for ch in s:
        if ch not in mapaS:
            mapaS[ch] = t[i]
        i += 1
  
    res = ''
    for ch in s:
        res += mapaS[ch]
 
    return res == t


s = "badc"
t = "baba"

print(isomorphic(s, t))