Password = str(input("Password: "))

while True:
    Repeat_Password = str(input("Repeat password: "))

    if Repeat_Password == Password:
        print("User account created!")
        break
    
    print("They do not match!")