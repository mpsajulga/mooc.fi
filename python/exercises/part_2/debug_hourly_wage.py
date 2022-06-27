hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily_wages = hourly_wage * hours
if day == "Sunday":
    daily_wages *= 2
    
print(f"Daily wages: {daily_wages} euros")