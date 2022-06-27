goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away :
    print("The home team won!")
elif goals_home < goals_away :
    print("The away team won!")
else:
    print("It's a tie!")