word = input("Word: ")
 
aligned = "*" + ( - len(word)) * " " + word + (14 - len(word)) * " " + "*"

print("*" * 30)
print(aligned)
print("*" * 30)