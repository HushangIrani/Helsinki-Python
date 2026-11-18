Fahrenheit = int(input("Please type in a temprature (F): "))
Celsius = (Fahrenheit - 32) / 1.8
print(f"{Fahrenheit} degrees Fahrenheit equals {Celsius} degrees Celsius")
if Celsius < 0:
    print("Brr! It's cold in here!")