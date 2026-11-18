print("What is the weather forecast for tomorrow?")
Temperature = int(input("Temperature: "))
Rain = str(input("Will it rain (yes/no): "))

if Temperature > 20:
    if Rain == "no":
        print("Wear jeans and a T-shirt")
    if Rain == "yes":
        print("Wear jeans and a T-shirt")
        print("Don't forget your umbrella!")

if Temperature > 10 and Temperature <= 20:
    if Rain == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
    if Rain == "yes":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Don't forget your umbrella!")

if Temperature > 5 and Temperature <= 10:
    if Rain == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
    if Rain == "yes":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Don't forget your umbrella!")

if Temperature <= 5:
    if Rain == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")
    if Rain == "yes":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")
        print("Don't forget your umbrella!")