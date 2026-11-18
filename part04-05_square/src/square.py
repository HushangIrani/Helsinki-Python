def line(length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

def square(size, character):
    width = size
    while size > 0:
        line(width, character)
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(3, "o")