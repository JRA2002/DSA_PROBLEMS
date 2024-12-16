'''Given an array of strings words, return the first palindromic
 string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.'''
def palindromic_string(words):
    for word in words:
            if len(word) == 1:
                return word
            i = 0
            j = len(word) - 1
            while i <= j+1:
                if word[i] == word[j]:
                    i += 1
                    j -= 1
                else:
                    break
                if i == j:
                    return word 
                elif i == j + 1:
                    return word
    return ""  

words = ["abc","car","ada","racecar","cool"]
res = palindromic_string(words)
print(res)

# Time Complexity:O(N*M)
# Auxiliary Space: O(N)