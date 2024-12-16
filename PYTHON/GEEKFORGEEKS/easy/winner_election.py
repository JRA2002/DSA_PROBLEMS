'''Given an array of n names arr of candidates in an election, 
where each name is a string of lowercase characters. A candidate
 name in the array represents a vote casted to the candidate. 
 Print the name of the candidate that received the maximum count
   of votes. If there is a draw between two candidates, then print lexicographically smaller name.'''

def winner(arr, n):
    dict1 = {}
    
    for name in arr:
        if name in dict1:
            dict1[name] += 1
        else:
            dict1[name] = 1

    maxi = 0
    nmax = ''
    for k, v in dict1.items():
        if v > maxi:
            maxi = v
            nmax = k  
        elif v == maxi and k < nmax:
            nmax = k
            maxi = v

    print(nmax, maxi)

arr = ["johne", "johnny", "johne", "johnny", "johne", "jackie", "johna", "johne", "johna", "johnny", "johna", "johnny", "johna"]
n = len(arr)

res = winner(arr, n)
print(res)