'''Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.'''

def valid_anagrams(strs: list):
    ans = []

    for w in range(len(strs)):
        actual = set(strs[w])
        res = []
        for ws in range(len(strs)):
            if actual == set(strs[ws]):
                res.append(strs[ws])
        ans.append(res)

    return ans


strs = ["eat","tea","tan","ate","nat","bat"]
print(valid_anagrams(strs))

