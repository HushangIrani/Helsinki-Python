word = str(input("Word: "))
print("*" * 30)
if ((28 - len(word))) % 2 == 0:
    print("*" + " " * ((28 - len(word)) // 2) + word + " " * ((28 - len(word)) // 2) + "*")
else:
    print("*" + " " * (((28 - len(word)) // 2)) + word + " " * (((28 - len(word)) // 2) + 1) + "*")
print("*" * 30)