print("Person 1:")
person1 = str(input("Name: "))
age1 = int(input("Age: "))
print("Person 2:")
person2 = str(input("Name: "))
age2 = int(input("Age: "))

if age1 > age2 :
    print(f"The elder is {person1}")
elif age1 < age2 :
    print(f"The elder is {person2}")
else :
    print(f"{person1} and {person2} are the same age")