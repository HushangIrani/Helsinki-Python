string = str(input("Please type in a string: "))
space = "*"

if len(string) >= 20:
    print(string)
else:
    print(f"{space * (20 - len(string))}{string}")