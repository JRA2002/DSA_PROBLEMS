'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.'''

def letter_combinations(digits: str):
    letters = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
            }
    
    ans = []

    def backtrack(s, currStr):
        if len(digits) == len(currStr):
            ans.append(currStr)
            return 
        
        for ch in letters[digits[s]]:
                backtrack(s + 1, currStr + ch)

    backtrack(0, "")

    
    return ans

digits = "23"

print(letter_combinations(digits))