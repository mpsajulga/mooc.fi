words = ""
safe_word2 = str(("") * 2)
word = input("Please type in a word: ")

while words != "end":
    words += word + " "
    word = str(word)
    
print(f"{words}")
    
