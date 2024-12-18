'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''

def valid_palindrome(s: str):
    i = 0
    j = len(s) - 1
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    while i < j:
        print(s[i],s[j])
        if s[i].lower() not in abc:
            i += 1
        if s[j].lower() not in abc:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = "A man, a plan, a canal: Panama"

print(valid_palindrome(s))
