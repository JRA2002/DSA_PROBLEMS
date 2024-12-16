def countString(string):
    count_alphabet = 0
    count_digits = 0
    count_symbol = 0

    for i in string:
        if i.isalpha():
            count_alphabet+=1
        elif i.isdigit():
            count_digits+=1
        else:
            count_symbol+=1

    print("Alphabets:",count_alphabet)
    print("Digits:",count_digits)
    print("Symbols:",count_symbol)

string = "hola11...."
countString(string)
