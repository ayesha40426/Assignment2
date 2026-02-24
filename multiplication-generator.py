number=int(input("enter number:"))
end=int(input("enter range:"))

print("multiplication table",number)

for i in range(1,end+2):
    print(number,"x",i,"=",number*i)
