'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).'''

def is_subsequence(s: str, t: str):
        if len(t) == 0 and len(s) > 0:
            return False
        elif len(s) == 0 and len(t) > 0:
            return True
        elif len(t) == 0 and len(s) == 0:
            return True
        ls = 0
        rs = len(s) - 1

        lt = 0
        rt = len(t) - 1

        res = ''
        while ls < rs:
            while lt < rt and t[lt] != s[ls]:
                lt += 1
            if t[lt] == s[ls]:
                res += t[lt]
                lt += 1
            ls += 1
        print(res)
        return res == s

s = "aaaaaa"
t = "bbaaaa"

print(is_subsequence(s, t))