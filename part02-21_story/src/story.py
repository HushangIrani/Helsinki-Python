story = ""
repeated_word = ""
story_continues = 0 

while True:
    word = str(input(" Please type in a word: "))

    if word == repeated_word:
        print(story)
        break

    if word != "end":
        story += word + " "
        story_continues += 1
        repeat = word
    else:
        print(story)
        break
    
    repeated_word = word