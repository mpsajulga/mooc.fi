input_width = int(input("Width: "))
input_height = int(input("Height: "))
hash = str("#")
width = hash*input_width
height = 0

while height < input_height:
    print(f"{width}")
    height += 1
    
