input_string = input("Please type in a string: ")
limit = -1*(1+len(input_string))
index = -1

while index != limit :
    print(input_string[index])
    index -= 1
