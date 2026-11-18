def spruce(size):
    number = 1
    height = size
    additive = 0
    print("a spruce!")

    if size == 1:
        additive = 1
    else:
        additive = size - 1

    while number <= size + additive:
        print((height - 1) * " ", end = "")
        print(number * "*")
        number += 2
        height -= 1
    print((size - 1) * " ", end = "")
    print("*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)