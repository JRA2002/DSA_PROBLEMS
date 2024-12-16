'''Given a string in roman form, the task is to convert this given roman string into an integer'''

def convert(s):
    romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
    result = 0
    i = 0

    while i < len(s):
        r1 = romans[s[i]]

        if i + 1 < len(s):
            r2 = romans[s[i+1]]
        else:
            r2 = 0
        if r1 > r2 :
            result = result + r1
        elif r1 == r2 :
            result = result + 2 * r1
            i += 1
        else:
            result = result + romans[s[i+1]] - romans[s[i]]
            i += 1
        i += 1
    
    return result


