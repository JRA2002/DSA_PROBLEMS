'''Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.'''

def replace_elements(arr: list):
    """
    Replace each element in the array with the greatest element among the elements to its right.
    The last element is replaced with -1.

    Parameters:
    arr (list): A list of integers.

    Returns:
    list: The modified list with elements replaced by the greatest element to their right.
    """
    n = len(arr)
    if n <= 1:
        return [-1]
    maxi= -1
    for i in range(n-1,-1,-1):
        temp = arr[i]
        arr[i] = maxi
        if temp > maxi:
            maxi = temp
    return arr

        

arr = [17,18,5,4,6,1]

res = replace_elements(arr)
print(res)