input_word = input("Please type in a word: ")
input_character = input("Please type in a character: ")

while True:
    if len(input_word) < 3:
        break
    print(input_word[0:3])
    input_word = input_word [2:]