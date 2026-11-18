def greatest_number(number1, number2, number3):
    if number1 > number2:
        result = number1
    else:
        result = number2

    if result < number3:
        result = number3

    return result


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(99, -4, 7)
    print(greatest)