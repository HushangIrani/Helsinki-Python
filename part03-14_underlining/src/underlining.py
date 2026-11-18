length = 1

while length > 0:
    string = str(input("Please type in a string: "))
    length = len(string)
    print(string)
    print("-" * len(string))