pins = ""
attempts = 0
master_pin = 4321

while True:
    pin = input("PIN: ")
    attempts += 1
    pins += pin + ", "
    
    if pin == "4321":
        success = True
        break
    if pin != 4321:
        print("Wrong")

if success:
    if attempts == 1:
        print(f"Correct! It only took you one single attempt!")
        print(f"{pins}")
    else:
        print(f"Correct! It took you {attempts} attempts")
        print(f"{pins}")