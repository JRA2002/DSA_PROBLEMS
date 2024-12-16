'''Given an array Arr[] of size N, print all the 
subsets of the array.

Subset: A subset of an array is a tuple that can be 
obtained from the array by removing some (possibly all) elements of it'''

def subsets(nums, n):
    #Function to find the subsets of the given array
    # Loop through all possible subsets using bit manipulation
    for i in range(1 << n):
        # Loop through all elements of the input array
        for j in range(n):
            #Check if the jth bit is set in the current subset
            if (i & (1 << j)) != 0:
                #If the jth bit is set, add the jth element to the subset
                print(nums[j], end=" ")
        print()

# using backtracking
def calcSubset(A, res, subset, index):
    # Add the current subset to the result list
    res.append(subset[:])

    # Generate subsets by recursively including and excluding elements
    for i in range(index, len(A)):
        # Include the current element in the subset
        subset.append(A[i])

        # Recursively generate subsets with the current element included
        calcSubset(A, res, subset, i + 1)

        # Exclude the current element from the subset (backtracking)
        subset.pop()


def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)
    return res

arr = [1, 2, 3]
n = len(arr)
subsets(arr, n)
