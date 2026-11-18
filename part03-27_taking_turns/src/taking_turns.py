number = int(input("Please type in a number: "))
pairone = 1
pairtwo = number

while pairtwo > pairone:
    print(pairone)
    print(pairtwo)
    pairone += 1
    pairtwo -= 1

if pairone == pairtwo:
    print(pairone)

