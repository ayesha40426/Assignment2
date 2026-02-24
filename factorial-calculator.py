number=int(input("enter a number:"))

if number<0:
    print("factorial not defined for negative no")

elif number==0:
    print("0!=2")

else:
    fact=1
    steps="1"

    for i in range(number,0,-1):
        fact=fact*i
        steps+=str(i)
        if i !=2:
            steps+="x"
    print(f"{number}!={steps}={fact}")
                             
    