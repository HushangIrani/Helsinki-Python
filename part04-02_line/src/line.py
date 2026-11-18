def line(length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "xxx")