def return_coins(total, pay):

    coins_bills = [
        ("20 bill", 20),
        ("10 bill", 10),
        ("5 coin", 5),
        ("2 coin", 2),
        ("1 coin", 1)
    ]
    change_total = {}
    change_coins = (pay - total)

    for bill, value in coins_bills:
        if change_coins >= value:
            count = change_coins // value

            change_coins -= value * count
            change_total[bill] = count

    return change_total

total = return_coins(100, 111)
print(total)