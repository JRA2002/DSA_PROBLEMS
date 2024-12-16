'''Given two strings of lowercase alphabets and a value k, the task is 
to find if two strings are K-anagrams of each other or not.
Two strings are called k-anagrams if following two conditions are true. 
Both have same number of characters.
Two strings can become anagram by changing at most k characters in a string.'''

def anagram(str1, str2, k):
    if len(str1) != len(str2):
        return False
    set1 = set(str1)
    set2 = set(str2)
    lista = []
    for i in set1:
        if i not in set2:
            lista.append(i)
    count = 0
    for i in lista:
        count += 1
    if count <= k:
        return True
    return False
    

res = anagram('geeks', 'eggkf', 1)
print(res)