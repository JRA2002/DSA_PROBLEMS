'''Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.

If the characters in str1 can be changed to get str2, then two strings, str1 and str2, 
are isomorphic. A character must be completely swapped out for another character
 while maintaining the order of the characters. A character may map to itself,
   but no two characters may map to the same character.'''
from collections import defaultdict
def is_isomorphic(str1, str2):
    dict1 = defaultdict(str)
    news = ''
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str2[i] not in dict1.values():
            dict1[str1[i]] = str2[i]
    print(dict1)
    for i in str1:
        news += dict1[i]
    print(((news)))
    if news == str2:
        return True
    return False  
    

str1 = 'ehj'
str2 = 'el'

res = is_isomorphic(str1, str2)
print(res)