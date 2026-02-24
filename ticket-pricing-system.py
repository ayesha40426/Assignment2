age = int(input("Enter your age: "))
day = input("Enter day: ")
tickets = int(input("Number of tickets: "))

if day in ["friday",
           "saturday", 
           "sunday"]:
    discount = base_price * 0.20
else:
    discount = 0

if age < 2:
    base_price =0
elif age <= 15:
    base_price = 100
elif age <= 25:
    base_price = 300
elif age <= 45:
    base_price = 400
elif age <= 56:
    base_price = 350
else:
    base_price = 250


base_price_after_discount = base_price - discount
total_amount = base_price_after_discount * tickets


print("Base Price of the movie ticket is:", base_price)
print("discount given to the movie ticket:", discount)
print("Price after giving discount to particular movie :", base_price_after_discount)
print("Total Amount of ticket:", total_amount)