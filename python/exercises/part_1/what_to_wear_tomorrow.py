print("What is the weather forecast for tomorrow? ")
temp = int(input("Temperature: "))
rain = str(input("Will it rain (yes/no): "))

if temp > 2:
    print("Wear jeans and a T-shirt")
    
if temp <21 >11 :
    print("I recommend a jumper as well")

if temp <11 >5:
    print("Take a jacket with you")

if temp  <=5 >2:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    
if rain == str("yes"):
    print("Don't forget your umbrella!")