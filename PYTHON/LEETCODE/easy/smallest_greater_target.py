'''You are given an array of characters letters that is sorted in 
non-decreasing order, and a character target. There are at least 
two different characters in letters.

Return the smallest character in letters that is lexicographically 
greater than target. If such a character does not exist, return the 
first character in letters.'''

def next_greater_letter(letters):
    i = 0
    j = len(letters) - 1

    while i <= j:
        midd = (i+j)//2
        if letters[midd] > target:
            j -= 1
        elif letters[midd] == target:
            if midd == j:
                print('yes')
                return letters[0]
            else:
                print('no')
                return letters[midd+1]
        else:
            i += 1
    if midd <= len(letters) - 1:
        if letters[midd] < target:
            return letters[0]
        return letters[midd]
    else:
        print(midd)
        return letters[0]

letters = ["c","e","j","l"]
target = 'n'

res = next_greater_letter(letters)
print(res)