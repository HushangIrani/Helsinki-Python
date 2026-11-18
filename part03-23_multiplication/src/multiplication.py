number = int(input("Please type in a number: "))
operandone = 0


while operandone < number:
    operandone += 1
    operandtwo = 0

    while operandtwo < number:
        operandtwo += 1
        print(f"{operandone} x {operandtwo} = {operandone * operandtwo}")
    