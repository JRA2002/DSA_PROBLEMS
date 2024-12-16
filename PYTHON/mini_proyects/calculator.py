def calculator():
    calculator = []

    while True:
        number = input("Enter :")
        if number == '=':
            break
        calculator.append(number)

    res = float(calculator[0])
    for i in range(len(calculator)-2):
        if calculator[i + 1] == '+':
            res = res + float(calculator[i + 2])
        if calculator[i + 1] == '-':
            res = res - float(calculator[i + 2])
        if calculator[i + 1] == '*':
            res = res * float(calculator[i + 2])
    return res
