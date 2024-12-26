'''Given a string s, find the length of the longest 
substring
 without repeating characters.'''

def length_substring_nonrepeating(s: str):
    
    maxC = 0
    for i in range(len(s)):
        count = 0
        mapa = {}
        for j in range(i, len(s)):
            if s[j] not in mapa:
                mapa[s[j]] = 1
                count += 1
            else:
                break
        maxC = max(maxC, count)

    return maxC

#optimal approach

s = "pwwkew"

print(length_substring_nonrepeating(s))