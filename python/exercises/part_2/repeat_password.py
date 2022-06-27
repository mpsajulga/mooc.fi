password1 = str(input("Password: "))
while True:
    password2 = str(input("Repeat password: "))
    
    if password2 != password1:
        print("They do not match!")
    if password2 == password1:
        break
print("User account created!")

