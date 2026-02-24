def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True



number=int(input("Enter a number: "))

if prime(number):
    print(number, "is prime number")
else:
    print(number, "is not a prime number")



s=int(input("Enter start range: "))
e=int(input("Enter end range: "))

print("Prime numbers:", end=" ")
for n in range(s, e + 1):
    if prime(n):
        print(n, end=" ")