'''Given a string s. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. s contains only lowercase letters.'''

def first_repeat_char(s: str):
    mapa = {}
    for ch in s:
        if ch not in mapa:
            mapa[ch] = 1
        else:
            return ch
        
    return -1

s = "gabcg"

print(first_repeat_char(s))