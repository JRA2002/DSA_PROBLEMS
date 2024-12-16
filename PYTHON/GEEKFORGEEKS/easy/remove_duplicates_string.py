'''Given a string str which may contain lowercase and uppercase characters. 
The task is to remove all duplicate characters from the string and
 find the resultant string. The order of remaining characters in 
 the output should be same as in the original string.'''

def remove_duplicates(str1):
    dict1 = {}
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    print(dict1)
    ans = ''
    for char in str1:
        if dict1[char] >= 1:
            ans += char
            dict1[char] = 0
            
        
    return ans

str1 = "geeksforgeeks"
res = remove_duplicates(str1)
print(res)