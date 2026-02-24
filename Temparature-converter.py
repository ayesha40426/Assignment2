while True:
    print("\nTemperature Converter======")
    print("1. celsius to fahrenheit")
    print("2. fahrenheit to celsius")
    print("3. celsius to kelvin")
    print("4. kelvin to celsius")
    print("5. fahrenheit to kelvin")
    print("6. kelvin to fahrenheit")
    print("7. exit")

    choice = input("Enter your choice(1-7) : ")

    if choice == "1":
        c = float(input("Enter celsius: "))
        print("fahrenheit:", (c * 9/5) + 32)

    elif choice == "2":
        f = float(input("Enter fahrenheit: "))
        print("celsius:", (f - 32) * 5/9)

    elif choice == "3":
        c = float(input("Enter celsius: "))
        print("kelvin:", c + 273.15)

    elif choice == "4":
        k = float(input("Enter kelvin: "))
        print("celsius:", k - 273.15)

    elif choice == "5":
        f = float(input("Enter fahrenheit: "))
        print("kelvin:", (f - 32) * 5/9 + 273.15)

    elif choice == "6":
        k = float(input("Enter kelvin: "))
        print("fahrenheit:", (k - 273.15) * 9/5 + 32)

    elif choice == "7":
      print("Exit prg.")
    
    

