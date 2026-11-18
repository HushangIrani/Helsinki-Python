def first_word(sentence):
    if sentence.find(" ") > 0:
        fword = sentence[0:sentence.find(" ")]
    else:
        fword = sentence
    return fword

def second_word(sentence):
    fword = first_word(sentence)
    remaining_sentence = sentence[len(fword) + 1:]

    if remaining_sentence.find(" ") > 0:
        sword = remaining_sentence[0:remaining_sentence.find(" ")]
        return sword
    elif len(remaining_sentence) > 0:
        sword = remaining_sentence
        return sword

def last_word(sentence):
    fword = first_word(sentence)
    sword = second_word(sentence)
    remaining_sentence = sentence[len(fword) + 1:]


    if remaining_sentence.find(" ") > 0:
        sword = remaining_sentence[0:remaining_sentence.find(" ")]
    elif len(remaining_sentence) > 0:
        sword = remaining_sentence

    if remaining_sentence.find(" ") > 0:
        while remaining_sentence.find(" ") > 0:
            nword = remaining_sentence[0:remaining_sentence.find(" ")]
            remaining_sentence = remaining_sentence[len(nword) + 1:]
    
    lword = remaining_sentence
    return lword

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence ="first"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))