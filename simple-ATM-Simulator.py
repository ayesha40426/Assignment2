acc_balance = 50000

while True:
    print("\n =====ATM SIMULATOR========")
    print("1. check balance")
    print("2. withdraw")
    print("3. deposit")
    print("4. exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
           amount=int(input("enter amount:"))
           print("current acc_balance:", acc_balance)
       

    elif choice == 2:
          amount = int(input("Enter amount to withdraw: "))
    if acc_balance-amount>=1000:
            acc_balance=acc_balance-amount
            print("Withdrawal successful!")
            print("Insufficient balance")

    elif choice == 3:
          amount = int(input("Enter deposit amount: "))
          acc_balance = acc_balance + amount
          print("deposit successful")
    
          print("new acc_balance:", acc_balance)

        
    elif choice == 4:
        print("exit")
        break

    else:
        print("Invalid")