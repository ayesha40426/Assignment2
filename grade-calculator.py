z1 = int(input("Enter marks for subject 1: "))
z2 = int(input("Enter marks for subject 2: "))
z3 = int(input("Enter marks for subject 3: "))
z4 = int(input("Enter marks for subject 4: "))
z5 = int(input("Enter marks for subject 5: "))

total = z1 + z2 + z3 + z4 + z5
percentage = (total / 500) * 100

print("Marks:", z1, z2, z3, z4, z5)
print("Total marks:", total)
print("Percentage:", percentage)


if z5 >= 40 and z4 >= 40 and z3 >= 40 and z2 >= 40 and z1 >= 40:
    result = "Finally passed🤩"
else:
    result = "again fail😂"

# grade
if percentage >= 95:
    grade = "A+"
elif percentage >= 85:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
print("Result:", result)