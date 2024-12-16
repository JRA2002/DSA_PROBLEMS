'''Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.'''

def common_chars(words: list):
    if len(words) == 1:
        return words[0]
    
    ans = []
    word1 = set(words[0])
    for char in word1:
        freq = min([word.count(char) for word in words])
        ans += [char]*freq

    return ans

      

#words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
words = ["bella","label","roller"]
print(common_chars(words))
