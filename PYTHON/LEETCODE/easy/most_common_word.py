'''Given a string paragraph and a string array of the banned 
words banned, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, 
and that the answer is unique.

The words in paragraph are case-insensitive and the answer 
should be returned in lowercase.'''
import re
from collections import Counter
def most_common_word(paragraph: str, banned: str):
    pattern = r'\w+'
    paragraph = paragraph.lower()
    res = re.findall(pattern, paragraph)
    dict1 = Counter(res)
    maxi = 0
    for char in dict1:
        if char not in banned and dict1[char] > maxi:
            maxi = dict1[char]
            res1 = char
    return res1


paragraph = "a"
banned = [""]


res = most_common_word(paragraph, banned)
print(res)