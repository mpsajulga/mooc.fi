points = int(input("How many points are on your card? "))
if points < 100:
    factor = 1.1
    print("Your bonus is 10 %")
    
if points >= 100:
    factor = 1.15
    print("Your bonus is 15 %")
 
# a *= b is the same thing as a = a * b
points *= factor
print("You now have", points, "points")