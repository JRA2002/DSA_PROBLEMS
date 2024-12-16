'''You are given an integer n and an integer array arr of size n+2. All elements of the array are in the range from 1 to n. Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
Note: Return the numbers in their order of appearing twice. So, if x and y are repeating numbers, and x's second appearance comes before the second appearance of y, then the order should be (x, y).'''

def two_repeated(n, arr):
        freq = [0] * (n + 1)
        ans = []
    
        for i in range(n+2):
            freq[arr[i]] = freq[arr[i]] + 1
            if freq[arr[i]] == 2:
                 ans.append(arr[i])
        return ans
# optimal approach

def two_repeated2(n, arr):
        res = []
        first = False

        #iterating over the array elements.
        for i in range(0, n + 2):
            print(arr)
            #making the visited elements negative.
            if arr[abs(arr[i])] > 0:
                arr[abs(arr[i])] = -arr[abs(arr[i])]

            #if the number is negative, it was visited previously
            #so this would be the repeated element.
            else:

                #storing first and second repeated element accordingly.
                if (first == False):
                    print(arr[abs(arr[i])])
                    res.append(abs(arr[i]))
                    first = True
                else:
                    res.append(abs(arr[i]))

        #returning the result.
        return res

arr = [1, 2, 2, 1]
n = len(arr) - 2
res = two_repeated2(n, arr)
print(res)