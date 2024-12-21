'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.'''

def word_pattern(pattern: str, s: str):
    hashP = {}
    hashS = {}
    i = 1
    for c in pattern:
        if c not in hashP:
            hashP[c] = str(i)
            i += 1
    s1 = ''
    for c in pattern:
        s1 += hashP[c]
        
    s = s.split(" ")
    i = 1
    s2 = ''
    for w in s:
        if w not in hashS:
            hashS[w] = str(i)
            i += 1
    for w in s:
        s2 += hashS[w]

    return s1 == s2

pattern = "abba"
s = "dog cat cat dog"

print(word_pattern(pattern, s))