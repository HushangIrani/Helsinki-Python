Students = int(input("How many students on the course? "))
Group_Size = int(input("Desired group size? "))
Groups = (Students + Group_Size - 1) // Group_Size
print("Number of groups formed:", Groups)