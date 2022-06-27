tax = 0.07 #that is, 7 percent
print("Enter the amount of each item.")
print("Enter 'quit' to end the program.")
amount = input("Amount of item? ")

while amount != "quit":
    amount = float(amount)
    total = (amount * tax) + amount
    print("The total for that item will be %.2f." % total)
    amount = input("Amount of item? ")
print("Thank you for using this progam.")