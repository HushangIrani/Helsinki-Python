ulimit = int(input("Upper limit: "))
number = 0

while ulimit - 1 > 0:
    number += 1
    print(number)
    ulimit -= 1