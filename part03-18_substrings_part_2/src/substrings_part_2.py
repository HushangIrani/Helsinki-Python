string = str(input("Please type in a string: "))
i = len(string)

while i >= 0:
    print(string[i:len(string)])
    i -= 1