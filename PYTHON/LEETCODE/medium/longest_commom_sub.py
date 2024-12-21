'''Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.'''

def longest_commom_sub(text1: str, text2: str):

    for i in range(1, len(text1)):
        print("holaaa")

text1 = "ab"
text2 = "ace"

longest_commom_sub(text1, text2)