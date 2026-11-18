string = str(input("Please type in a string: "))
index = 0
character = len(string)

while index < len(string):
    print(string[character - 1])
    index += 1
    character -= 1
