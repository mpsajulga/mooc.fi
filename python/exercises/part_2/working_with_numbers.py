print("Please type in integer numbers. Type in 0 to finish.")
count = 0
number = 0
zero_day = 0
positive_numbers = 0
negative_numbers = 0

while True:
    inp_number = int(input("Number: "))
    
    if inp_number <0:
        negative_numbers += 1
    if inp_number >0:
        positive_numbers += 1
    
    if inp_number == zero_day:
        break
    number += inp_number
    count += 1
    
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {number}")
print(f"The mean of the numbers is {number/count}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")