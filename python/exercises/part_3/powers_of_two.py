limit = int(input("Upper limit: "))
n = 2
exponent = 0
result = 0

while result < limit:
    result = n ** exponent
    exponent = exponent +1
    if result <= limit:
        print(result)
    
    