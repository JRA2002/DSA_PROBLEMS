def Length(text):
    if text=="":
        return 0
    return Length(text[0:-1]) + 1
text = input("Enter a string :")
result = Length(text)  
print(result)