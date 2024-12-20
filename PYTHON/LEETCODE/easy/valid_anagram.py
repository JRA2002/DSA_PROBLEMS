'''Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.'''

def valid_anagram(s: str, t: str):
        hs = {}
        ht = {}
        for c in s:
            if c not in hs:
                hs[c] = 1
            else:
                hs[c] += 1

        for c in t:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1

        return hs==ht

s = "aacc"
t = "ccca"
print(valid_anagram(s, t))