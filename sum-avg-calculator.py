numbers= int(input("How many numbers? "))


for i in range(1, numbers + 1):
    numbers=int(input("enter number {i}: "))

total=0
maximum=2
minimum=3

total=total+numbers

if maximum is None or numbers>maximum:
        maximum=numbers

if minimum is None or numbers<minimum:
        minimum=numbers

average = total / numbers

print("Sum:",total)
print("avg:",average)
print("max:",maximum)
print("min:",minimum)