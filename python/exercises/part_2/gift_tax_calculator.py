gift = int(input("Value of gift: "))

tax1 = 100+(gift-5000)*0.08
tax2 = 1700+(gift-25000)*0.10
tax3 = 4700+(gift-55000)*0.12
tax4 = 22100+(gift-200000)*0.15
tax5 = 142100+(gift-1000000)*0.17

if gift >= 5000 and gift <= 25000:
    print(f"Amount of tax: {tax1} euros")
elif gift >= 25000 and gift <= 55000:
    print(f"Amount of tax: {tax2} euros")
elif gift >= 55000 and gift <= 200000:
    print(f"Amount of tax: {tax3} euros")
elif gift >= 200000 and gift <= 1000000:
    print(f"Amount of tax: {tax4} euros")
elif gift >= 1000000:
    print(f"Amount of tax: {tax5} euros")
else:
    print("No tax!")