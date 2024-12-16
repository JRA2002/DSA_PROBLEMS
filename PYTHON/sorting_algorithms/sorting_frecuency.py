'''Print the elements of an array in the decreasing frequency 
if 2 numbers have the same frequency then print the one which came first'''

from collections import defaultdict

def sortByFreq(arr, n):
    # arr -> Array to be sorted
    # n   -> Length of Array

    # d is a hashmap(referred as dictionary in python)
    d = defaultdict(lambda : 0)
    print(d)
    for i in range(n):
        d[arr[i]] += 1
        print(d)

    # Sorting the array 'arr' where key
    # is the function based on which
    # the array is sorted
    # While sorting we want to give
    # first priority to Frequency
    # Then to value of item
    arr.sort(key=lambda x: (-d[x], x)) 
    #require Updation:- reverse = True, to sort an array in descending order
    return arr


# Driver code
if __name__ == "__main__":
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    n = len(arr)

    # Function call
    solution = sortByFreq(arr, n)
    print(solution)


