# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    print("Your bonus is 10 %")
    print("You now have", points * 1.1, "points")

if points >= 100:
    print("Your bonus is 15 %")
    print("You now have", points * 1.15, "points")