let1 = str(input("1st letter: "))
let2 = str(input("2nd letter: "))
let3 = str(input("3rd letter: "))

if let1 >= let2 and let1 <= let3 or let1 >= let3 and let1 <= let2:
    print(f"The letter in the middle is {let1}.")
elif let2 >= let1 and let2 <= let3 or let2 >= let3 and let2 <= let1:
    print(f"The letter in the middle is {let2}.")
elif let3 >= let1 and let3 <= let2 or let3 >= let2 and let3 <= let1:
    print(f"The letter in the middle is {let3}.")