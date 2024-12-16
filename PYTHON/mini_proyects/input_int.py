
def formula(a, b, c):
    d = a + b
    if isinstance(a, int):
        if c == d:
            print(d)
            return True
        else:
            return False
    else:
        return "Not integer as input"
        
        
a = int(input("enter first int : "))
b = int(input("enter second int : "))
c = int(input("enter third int : "))

result = formula(a, b, c)

print(f"the numbers can be used by this formula “a+b = c,” ?? : {result}")