'''You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.'''

def find_majority(arr: list):
    mapa = {}
    res = []
    for num in arr:
        if num not in mapa:
            mapa[num] = 1
        else:
            mapa[num] += 1
            
    for k, v in mapa:
        if v > len(arr) // 3:
            res.append(k)
    res.sort()

    return res


arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]

print(find_majority(arr))