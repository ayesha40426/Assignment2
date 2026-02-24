try:
    subtotal = float(input("Enter bill subtotal amount: "))
    tax_percentage = float(input("Enter tax percentage: "))
    tip_percentage = float(input("Enter tip percentage: "))
    number_of_people = int(input("Enter number of people: "))

    if subtotal < 0 or tax_percentage < 0 or tip_percentage < 0:
        print("Amounts and percentages cannot be negative.")
    
    elif number_of_people <= 0:
        print("Number of persons should be greater than zero.")
    
    else:
       
        tax_amount = subtotal * tax_percentage / 100
        amount_after_tax = subtotal + tax_amount


        tip_amount = amount_after_tax * tip_percentage / 100
        total_bill = amount_after_tax + tip_amount

       
        amount_per_person = total_bill / number_of_people

        print("\n=== BILL SUMMARY ====")
        print("Subtotal:", subtotal)
        print("Tax Amount:", round(tax_amount, 3))
        print("Tip Amount:", round(tip_amount, 3))
        print("Total Bill:", round(total_bill, 3))
        print("Each Person Pays:", round(amount_per_person, 2))

except ValueError:
    print("Invalid input. Please enter numeric values only.")