'''Given an array of N integers where each value represents the 
number of chocolates in a packet. Each packet can have a variable 
number of chocolates. There are m students, the task is to distribute 
chocolate packets such that: 

Each student gets one packet.
The difference between the number of chocolates in the packet with 
maximum chocolates and the packet with minimum chocolates given 
to the students is minimum.'''

def chocolate_distribution(arr : list, m):
    arr.sort()
    min_diff = arr[0:m][-1] - arr[0:m][0]
    
    for i in range(1, len(arr) - m + 1):
        new = arr[i:m+i]
        diff = new[-1] - new[0]
        if min_diff >= diff:
            min_diff = diff
        
    return min_diff

arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
res = chocolate_distribution(arr, 7)
print(res)