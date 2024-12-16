'''Given a string str without spaces, the task is to remove 
all duplicate characters from it, keeping only the first occurrence.

Note: The original order of characters must be kept the same. '''

def remove_duplicates(str1):
    i = 0
    new = ''
    
    while i <= len(str1) - 1:
        if str1[i] not in str1[:i]:
            new += str1[i]
        i += 1
    return new
str1 = 'svvvg'
res = remove_duplicates(str1)
print(res)