phrase = ""
safe_word = "end"
previous_word = None

while True:
    input_word = input("Please type in a word: ")
    
    if input_word == safe_word or input_word == previous_word:
        break
    
    previous_word = input_word
    
    phrase += input_word + " "

print(phrase)
    