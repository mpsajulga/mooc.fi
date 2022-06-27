# hourly_wage = float(input("Hourly wage: "))
# hours = int(input("Hours worked: "))
# day = input("Day of the week: ")

hourly_wage = 20.0
hours = 6
day = "Sunday"

daily_wages = hourly_wage * hours
if day == "sunday":
    daily_wages * 2
    
print(f"Daily wages: {daily_wages} euros")