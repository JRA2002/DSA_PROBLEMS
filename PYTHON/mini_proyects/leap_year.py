year = int(input("Enter a year :"))

if year%400==0:
    print("LEAP YEAR")
elif year%100==0:
    print("NOOO LEAP")
elif year%4==0:
    print("LEAP YEAR")
else:
    print("NOOO LEAP")        