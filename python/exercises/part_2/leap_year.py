year = int(input("Please type in a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("That is a leap year.")
    else:
        print("That is not a leap year.")
elif year % 4 == 0:
    print("That is a leap year.")
else:
    print("That is not a leap year.")
    