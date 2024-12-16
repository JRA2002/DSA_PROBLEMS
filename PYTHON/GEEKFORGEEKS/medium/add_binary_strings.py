'''Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.'''

def add_binary(s1: str, s2: str):
    
    res = ''
    mapa = {"11":"0", "01":"1", "1":"1", "00":"0", "101":"0", "111":"1"}
    
    m = len(s1) - 1
    n = len(s2) - 1
    k = ""
    midd = ""
    if m >= n:
        while n >= 0:
            
            ch1 = s1[m]
            ch2 = s2[n]
            
            if k + ch1 + ch2 == "11" or k + ch1 + ch2 == "101" or k + ch1 + ch2 == "111":
                
                midd = mapa[k + ch1 + ch2]
                k = "1"
            print(ch1,ch2,k)
            res = k + midd + res
            
            m -= 1
            n -= 1

        while m >= 0:
            print(m,n)
            res = s1[m] + res
            m -= 1
            
    return res

s1 = "10"
s2 = "10"

res = add_binary(s1, s2)
print(res)