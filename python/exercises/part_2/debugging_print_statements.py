# ...

hourly_wage = 20.0
hours = 6
day = "Sunday"

daily_wages = hourly_wage * hours
print("condition:", day == "Sunday")
if day == "Sunday":
    print("wages before:", daily_wages)
    daily_wages *= 2
    print("wages after doubling:", daily_wages)

print(f"Daily wages: {daily_wages} euros")