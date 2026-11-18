while True:
    number = int(input("Please type in a number: "))
    factorial = 1
    operand = number

    if number <= 0:
        print("Thanks and bye!")
        break
    else:
        while operand >= 1:
            factorial = factorial * operand
            operand -= 1
    print("The factorial of the number", number, "is", factorial)