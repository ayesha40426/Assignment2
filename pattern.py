pattern = int(input("Enter pattern number: "))
h = int(input("Enter height: "))


if pattern == 1:
    for i in range(1, h+1):
        for j in range(i):
            print(i, end=" ")
        print()


elif pattern == 2:
    for i in range(1, h+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

elif pattern == 3:
    for i in range(1, h+2):
        for j in range(1, i+1+1):
            print(j, end=" ")
        print()

elif pattern == 4:
    for i in range(1, h-1):
        for j in range(1, i+2):
            print(j, end=" ")
        print()

 