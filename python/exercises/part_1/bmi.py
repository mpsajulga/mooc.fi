height = 172.5
weight = 68.55

# the Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
# height is converted into metres in the formula

bmi = weight/(height/100) ** 2
print(f"The BMI is {bmi}")