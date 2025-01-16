'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.'''

from collections import defaultdict

def can_construct(ransomNote: str, magazine: str):

    if len(ransomNote) > len(magazine):
        return False
    
    mapR = {}
    for ch in ransomNote:
        if ch not in mapR:
            mapR[ch] = 1
        else: 
            mapR[ch] += 1
    mapM = {}

    for ch in magazine:
        if ch not in mapM:
            mapM[ch] = 1
        else: 
            mapM[ch] += 1

    for ch, val in mapR.items():
        if ch not in mapM or val > mapM[ch]:
            return  False
       
    return True


    

    

ransomNote = "aaabc"
magazine = "baacdfg"

print(can_construct(ransomNote, magazine))