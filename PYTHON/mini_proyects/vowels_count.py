string = "Aalelsfdfsdfusoiidskdoca"

def vowels_count(lista):
    vowels = ["a","e","i","o","u"]
    count = 0

    for st in string:
        if st in vowels:
            count +=1
    return count

count = vowels_count(string)
print(count)