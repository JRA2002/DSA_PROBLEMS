'''Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.'''

from collections import defaultdict

def valid_anagrams(strs: list):
    ans = defaultdict(list)
    
    for w in strs:
        count = [0] * 26
        for ch in w:
            count[ord(ch) - ord('a')] += 1
        ans[tuple(count)].append(w)
    
    return [val for val in ans.values()]


strs = ["eat","tea","tan","ate","nat","bat"]
print(valid_anagrams(strs))

