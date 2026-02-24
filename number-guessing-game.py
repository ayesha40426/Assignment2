import random

n=random.randint(1,100)
attempts=10

print("guess the number from 1 and 100")

while attempts>0:
    guess = int(input("Enter your guess: "))
    if guess==n:
        print("Correct! You won 🎉")
        break
    elif guess>n:
        print("Too high")
    else:
        print("Too low")

    attempts-=1
    print("remaining attempts:", attempts)

if attempts==0:
    print("congratulation! score:", n)