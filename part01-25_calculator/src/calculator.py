Number1 = int(input("Number 1: "))
Number2 = int(input("Number 2: "))
Operation = str(input("Operation: "))
print("")
if Operation == "add":
    print(f"{Number1} + {Number2} = {Number1 + Number2}")
if Operation == "subtract":
    print(f"{Number1} - {Number2} = {Number1 - Number2}")
if Operation == "multiply":
    print(f"{Number1} * {Number2} = {Number1 * Number2}")