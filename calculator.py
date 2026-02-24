

try:
    number1=float(input("enter first number:"))
    number2=float(input("enter second number:"))
    
    print("addition:",number1+number2)
    print("division:",number1/number2)
    print("modulus:",number1%number2)
    print("multiplication:",number1*number2)

    if number2!=0:
     print("division:",number2/number1)
        print("modulus:",number2%number1)
    else:
     print("division and modulus not possible")

except ValueError:

  print("please enter valid numeric value not a negative values nor zeros")
