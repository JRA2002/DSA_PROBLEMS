'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''

def valid_palindrome(s: str):
    i = 0
    j = len(s) - 1
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while i < j:
        
        while i < j and s[i].lower() not in abc:
            i += 1
        while i < j and s[j].lower() not in abc:
            j -= 1

        if s[i].lower() != s[j].lower():
            print(s[i], s[j])
            return False
        else:
            i += 1
            j -= 1

    return True

def valid_palindrome2(s: str):
    def isalnum(c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not isalnum(s[i]):
            i += 1
        while i < j and not isalnum(s[j]):
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1  
            
    return True

s = ",."

print(valid_palindrome2(s))
