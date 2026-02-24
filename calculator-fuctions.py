def calculator():
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
a=int(input("Enter first num:"))
b=int(input("Enter second num:"))

def addition(a,b):
    print("res:",a+b)

def subtraction(a,b):
    print("res:",a-b)

def multiplication(a,b):
    print("res:",a*b)

def division(a,b):
    if b==0:
        print("cannot divide by zeros")
    else:
        print("res:",a/b)

        choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exit")
        return
    
    if choice==1:
        addition(a,b)
    elif choice==2:
        subtraction(a,b)
    elif choice==3:
        multiplication(a,b)
    elif choice==4:
        division(a,b)
    else:
        print("Wrong")



calculator()
    
   

