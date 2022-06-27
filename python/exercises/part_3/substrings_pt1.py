string = input("Please type in a string: ")
 
length = 1
while length <= len(string):
    print(string[0:length])
    length += 1