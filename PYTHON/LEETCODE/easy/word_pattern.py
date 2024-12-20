'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.'''

def word_pattern(pattern: str, s: str):
    hashP = {}
    for c in pattern:
        if c not in hashP:
            hashP[c] = ord(c)

    print(hashP)

pattern = "abba"
s = "dog cat cat dog"

print(word_pattern(pattern, s))