fah = int(input("Please type in a temperature (F): "))
cel = (fah-32) * (5/9)

print(f"{fah} degrees Fahrenheit equals {cel} degrees Celsius")

condition = cel <= 0
if condition:
    print("Brr! It's cold in here!")