'''Given a string Str. The task is to check if it is Pangram or not. 
A pangram is a sentence containing every letter in the English Alphabet.'''

def panagram(s: str):
    s = s.lower()
    set1 = set(s)
    suma = 0
    
    for char in set1:
        if ord(char) >= 97 and ord(char) <= 122:
            suma += 1
    if suma == 26:
        return 1
    return 0

res = panagram('The quick brown fox jumps over the dog')
print(res)