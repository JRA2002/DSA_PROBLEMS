'''Two strings str1 and str2 are called isomorphic if there is 
a one-to-one mapping possible for every character of str1 to every 
character of str2. And all occurrences of every character in str1
map to the same character in str2.'''

from collections import defaultdict
def ismorphic(str1, str2):
    if len(str1) != len(str2):
        return -1
    
    lst1 = []
    lst1.append(str1[0])
    num1 = []
    lst2 = []
    lst2.append(str2[0])
    num2 = []
    j = 1
    
    dict1 = defaultdict(int)
    
    return dict1['a']

res = ismorphic('aabb','ffgg')
print(res)