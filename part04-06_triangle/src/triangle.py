def line(length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

def triangle(size):
    width = 1
    while width <= size:
        line(width, "#")
        width += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
