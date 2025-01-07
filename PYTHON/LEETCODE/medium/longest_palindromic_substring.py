'''Given a string s, return the longest 
palindromic
 
substring
 in s.'''

def longest_palindromic_subs(s: str):
    def is_palindrome(l, r, res, maxL):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > maxL:
                res = s[l:r+1]
                maxL = r - l + 1
            l -= 1
            r += 1

        return res, maxL

    res = ''
    maxL = 0
    for i in range(len(s)):
        # odd length
        res, maxL = is_palindrome(i, i, res, maxL)

        # even length
        res, maxL = is_palindrome(i, i+1, res, maxL)

    return res
        
def longest_palindromic_subs2(s: str):
    def is_palindrome(l, r, count):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count

    count = 0
    for i in range(len(s)):
        # odd length
        count = is_palindrome(i, i, count)

        # even length
        count = is_palindrome(i, i+1, count)

    return count


s = "abcdeff"

print(longest_palindromic_subs2(s))