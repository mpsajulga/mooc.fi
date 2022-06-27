wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")

   
if day == "Sunday":
    daily_wage = float(wage*2*hours)
    print(f"Daily wages: {daily_wage} euros")

if day != "Sunday":
    daily_wage = float(wage*hours)
    print(f"Daily wages: {daily_wage} euros")

