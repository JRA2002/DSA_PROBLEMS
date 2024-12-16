'''Given a string s consisting of lowercase Latin Letters. 
Return the first non-repeating character in s. If there is 
no non-repeating character, return '$'.

Note : When you return '$' driver code will output -1.'''
from collections import defaultdict
def non_repeating_character(s):
    dict1 = defaultdict(str)
    for char in s:
        if dict1[char]:
            dict1[char] += 1
        else:
            dict1[char] = 1
            
    for char in s:
        if dict1[char] == 1:
            return char


s = 'zxvczbtxyzvy'
res = non_repeating_character(s)
print(res)