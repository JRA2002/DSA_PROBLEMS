'''Given a string S, check if it is palindrome or not.'''

def is_palindrome(S):
    i = 0
    j = len(S) - 1
    while i < j:
        if S[i] != S[j]:
            return False
        i += 1
        j -= 1
    return True

S  = 'abba'
res = is_palindrome(S)
print(res)