string_1 = str(input("Please type in a string 1: "))
string_2 = str(input("Please type in a string 2: "))
lenght_1 = len(string_1)
length_2 = len(string_2)

if lenght_1 > length_2:
    print(f"{string_1} is longer")
elif lenght_1 == length_2:
    print("The strings are equally long")
else:
    print(f"{string_2} is longer")

    