year = int(input("Please type in a year: "))

if year % 100 == 0 and year % 400 != 0:
    print("This year is not a leap year.")
elif year % 4 != 0:
    print("This is not a leap year.")
else:
    print("This is a leap year.")