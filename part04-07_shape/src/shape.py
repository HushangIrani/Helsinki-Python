def line(length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

def shape(tsize, tcharacter, rsize, rcharacter):
    twidth = 1
    while twidth <= tsize:
        line(twidth, tcharacter)
        twidth += 1
    while rsize > 0:
        line(tsize, rcharacter)
        rsize -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")