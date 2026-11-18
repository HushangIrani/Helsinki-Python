number = int(input("Please type in a number: "))
pairone = 0
pairtwo = 0

while pairtwo < number - 1:
    pairone = pairtwo + 1
    pairtwo = pairone + 1
    print(pairtwo)
    print(pairone)

if number %2 != 0:
    print(number)