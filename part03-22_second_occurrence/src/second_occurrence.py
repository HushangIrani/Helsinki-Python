string = str(input("Please type in a word: "))
substring = str(input("Please type in a substring: "))
count = 1
index = -1
firstindexamount = 0
secondindexamount = 0

while count <= 2:
    index = string.find(substring)

    if index < 0:
        break

    if count == 1 and index == 0:
        firstindexamount = len(substring)
        string = string[len(substring):]
        count += 1
    elif count == 1 and index > 0:
        firstindexamount = index + len(substring)
        string = string[firstindexamount:]
        count += 1
    elif count == 2 and index == 0:
        secondindexamount = index
        count += 1
    elif count == 2 and index > 0:
        secondindexamount = index
        count += 1

if count == 3:
    print(f"The second occurrence of the substring is at index {firstindexamount + secondindexamount}.")
else:
    print("The substring does not occur twice in the string.")