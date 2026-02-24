year = int(input("Enter year: "))

if year % 4 == 0:
 print(year, "leap year")
 print("reason: divisible by 4 and does 100/400 rule")

elif year % 100 != 0:
 print(year, "not leap year")
 print("reason: not suitable for leap year conditions")

else :year % 400 == 0
print(year, "not leap year")
print("reason: not suitable for leap year conditions")
  
  