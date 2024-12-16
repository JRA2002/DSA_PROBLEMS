def take_input():

    num = 0
    while num <= 2:
        num = int(input("Enter a number > 2 :"))
        if num <= 2:
            print("wrong number must be > 2 again...")
        else:
            count = 0
            while num > 2:
                num = num / 2
                count += 1
            break
    return count

count = take_input()
print(count)
