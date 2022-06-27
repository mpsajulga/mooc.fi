string_input = str(input("Please type in a string: "))
hash = "*"
hash_length = len(hash)
lenghth_of_string = len(string_input)


while hash_length + lenghth_of_string < 20:
    hash_length += 1
    hash += "*"

print(hash+string_input)