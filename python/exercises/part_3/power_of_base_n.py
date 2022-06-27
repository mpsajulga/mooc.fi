limit = int(input("Upper limit: "))
n = int(input("Base: "))

exponent = 0
result = 0

while result < limit:
    
    result = n ** exponent
    exponent = exponent +1
    print(result)
