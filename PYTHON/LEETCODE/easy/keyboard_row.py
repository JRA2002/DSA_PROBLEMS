'''Given an array of strings words, return the words that 
can be typed using letters of the alphabet on only one row 
of American keyboard like the image below.
In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".'''


def keyboard_row(words):
    row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
    res = []
    for word in words:
        w = set(word.lower())
        if w <= row1 or w <= row2 or w <= row3:
            res.append(word)
    return res

words = ["Hello","Alaska","Dad","Peace"]
res = keyboard_row(words)
print(res)