print("Please type in integer numbers. Type in 0 to finish.")
number_count = 0
sum = 0
mean = 0
positive_count = 0
negative_count = 0

while True:
    number = int(input("Number: "))

    if number != 0:
        number_count += 1
        sum += number
        if number > 0:
            positive_count += 1
        else:
            negative_count += 1
    else:
        print("Numbers typed in", number_count)
        print("The sum of the numbers is", sum)
        print("The mean of the numbers is", sum/number_count)
        print("Positive numbers", positive_count)
        print("Negative numbers", negative_count)
        break