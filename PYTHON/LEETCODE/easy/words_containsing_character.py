'''You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.'''

def find_words(words: list, x: str):
    res = []
    i = 0
    for word in words:
        for char in word:
            if char == x:
                res.append(i)
                break
        i += 1

    return res

words = ["leet","code"]
x = "e"

res = find_words(words, x)
print(res)
