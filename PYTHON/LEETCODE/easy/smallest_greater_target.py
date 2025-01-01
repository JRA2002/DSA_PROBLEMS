'''You are given an array of characters letters that is sorted in 
non-decreasing order, and a character target. There are at least 
two different characters in letters.

Return the smallest character in letters that is lexicographically 
greater than target. If such a character does not exist, return the 
first character in letters.'''

def next_greater_letter(letters):
        l = 0 
        r = len(letters) - 1

        while l <= r:
            m = (l+r)//2
            if letters[m] == target:
                while m+1 <= len(letters) - 1 and letters[m+1] == target:
                    m += 1
                if m == len(letters) - 1:
                    return letters[0]
                else:
                    return letters[m+1]
            elif letters[m] < target:
                l = m + 1
            else:
                r = m - 1
    
        if target < letters[m] and m == 0:
            return letters[0]
        if target > letters[m]:
            if m == len(letters) - 1 :
                return letters[0]
            else:
                return letters[m+1]
        else:
            return letters[m]

letters = ["c","e","j","l"]
target = 'n'

res = next_greater_letter(letters)
print(res)