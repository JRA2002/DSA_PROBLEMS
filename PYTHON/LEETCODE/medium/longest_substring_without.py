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

def length_substring_nonrepeating2(s: str):
    
    ans = set()
    l = 0
    maxC = 0
    for c in range(len(s)):
        while s[c] in ans:
            ans.remove(s[l])
            l += 1
        ans.add(s[c])
        maxC = max(maxC, c - l + 1)
    return maxC


s = "pwwkew"

print(length_substring_nonrepeating2(s))