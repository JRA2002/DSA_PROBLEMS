'''Given a number, find its corresponding Roman numeral.'''

def romans(res):
    if res == 1:
        return 'I'
    elif res == 4:
        return 'IV'
    elif res == 5:
        return 'V'
    elif res == 9:
        return 'IX'
    elif res == 10:
        return 'X'
    elif res == 40:
        return 'XL'
    elif res == 50:
        return 'L'
    elif res == 90:
        return 'XC'
    elif res == 100:
        return 'C'
    elif res == 400:
        return 'CD'
    elif res == 500:
        return 'D'
    elif res == 900:
        return 'CM'
    elif res == 1000:
        return 'M'
    return False
    
def convert_roman(num):
  
    string = ''

    while num != 0:
        if romans(num):
            string += romans(num)
            num = num % num
        else:
            if num > 1000:
                quo = num // 1000
                num = num % 1000
                string += romans(1000) * quo
            elif num > 900:
                num = num % 900
                string += romans(900)
            elif num > 500:
                num = num % 500
                string += romans(500) 
            elif num > 400:
                num = num % 400
                string += romans(400)
            elif num > 100:
                num = num % 100
                string += romans(100) 
            elif num > 90:
                num = num % 90
                string += romans(90) 
            elif num > 50:
                num = num % 50
                string += romans(50) 
            elif num > 40:
                num = num % 40
                string += romans(40)     
            elif num > 10:
                num = num % 10
                string += romans(10)     
            elif num > 9:
                num = num % 9
                string += romans(9) 
            elif num > 5:
                num = num % 5
                string += romans(5)          
            elif num > 4:
                num = num % 4
                string += romans(4)     
            elif num >= 1:
                num = num - 1
                string += romans(1)
    return string
            
    

res =convert_roman(3)
print(res)
a = [1, 2, 3, 4, 5, 8, 8, 8, 9, 10]
set1 = set(a)
b = len(set1)
print(b)

