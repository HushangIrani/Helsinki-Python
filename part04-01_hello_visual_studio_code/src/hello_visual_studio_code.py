# Write your solution here
while True:
    editor = str(input("Editor: "))

    if "visual studio code" == editor.lower():
        print("an excellent choice!")
        break
    elif editor.lower() == "word" or editor.lower() == "notepad":
        print("awful")
    else:
        print("not good")