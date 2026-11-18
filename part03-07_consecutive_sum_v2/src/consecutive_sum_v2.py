limit = int(input("Limit: "))
number = 1
total = 0
text = ""

while total < limit:
    total += number
    if total >= limit:
        text += f"{number} "
    else:
        text += f"{number} + "
    number += 1

print(f"The consecutive sum: {text} = {total}")