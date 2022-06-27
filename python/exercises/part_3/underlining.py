mask = str("-")

while True:
        string_input = str(input("Please type in a string: "))
        lenghth_of_string = len(string_input)
        if lenghth_of_string > 0:
            print(string_input)
            print(f"{mask*lenghth_of_string}")
        elif lenghth_of_string == 0:
            break