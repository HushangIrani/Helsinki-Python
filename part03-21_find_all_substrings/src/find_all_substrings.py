word = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))

while True:
    index = word.find(character)

    if index < 0:
        break

    if len(word) - index >= 3:
        print(word[index:index + 3])
        word = word[index + 1:]
    else:
        break