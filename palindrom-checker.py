number=input("Enter number: ")

real=number
reversed_number = number[::-1]

print("real:", real)
print("Reversed:", reversed_number)

if real==reversed_number:
    print("res:palindrome")
else:
    print("res:not a palindrome")