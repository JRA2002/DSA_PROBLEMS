'''You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
abc
bce
cae
You want to delete the columns that are not sorted lexicographically. 
In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') 
are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.'''

def min_delketion_size(strs):
    j = 0
    count = 0
    for i in range(len(strs) - 1):
        print(strs[i][j])
        print(strs[i+1][j])
        for k in 
    return count
strs = ["cba","daf","ghi"]
res = min_delketion_size(strs)
print(res)