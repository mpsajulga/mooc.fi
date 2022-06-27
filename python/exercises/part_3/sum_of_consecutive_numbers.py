limit = int(input("Limit: "))
number = 1
result = 1
verdict = "1" + " "

while limit > result :
    number += 1
    verdict += (f"+ {number} ")
    result += number
    
print(f"The consecutive sum: {verdict} = {result}")