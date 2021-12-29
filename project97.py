import random
number=random.randint(1,9)
chances=0
print("Guess a number between 1 to 10")
while chances<3:
    guess=int(input("Enter a number: "))
    if(guess==number):
        print("You win!!")
        break
    elif(guess<number):
        print("Please guess a bigger number")
    else:
        print("Please guess a smaller number")
    chances=chances+1
if(not chances<3):
    print("You loose")