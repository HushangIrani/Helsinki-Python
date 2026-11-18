# Write your solution here
def chessboard(length):
    row = 1
    height = 1
    print_value = 1
    last_print_value = 0
    while height <= length:
        while row <= length:
            print(print_value, end = "")
            last_print_value = print_value
            if print_value == 1:
                print_value = 0
            else:
                print_value = 1

            row += 1
        if length % 2 == 0:
            print_value = last_print_value
        row = 1
        height += 1
        print()


# Testing the function
if __name__ == "__main__":
    chessboard(4)
