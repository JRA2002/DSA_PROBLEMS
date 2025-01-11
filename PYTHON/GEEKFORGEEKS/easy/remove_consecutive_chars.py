'''You are given a string s, consisting of lowercase alphabets. Your task is to remove consecutive duplicate characters from the string. '''

def remove_consecutive_chars(s: str):
    stack = []
    init = s[0]
    res = ''
    for ch in s:
        stack.append(ch)
        if stack:
            out = stack.pop()
            
        if init != out:
            res = res + init
            init = out

    return res+out

s = "aabaa"

print(remove_consecutive_chars(s))