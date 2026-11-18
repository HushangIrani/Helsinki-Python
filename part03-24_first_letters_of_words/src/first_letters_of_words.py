sentence = str(input("Please type in a sentence: "))
spaceindex = 1

while spaceindex > 0:
    print(sentence[0])
    spaceindex = sentence.find(" ")
    sentence = sentence[spaceindex + 1:]
