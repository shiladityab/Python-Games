print("Guess a Number between ZERO to TEN Game")

import random

number = random.randint(0,10)

guess = int(input("I am thinking about the number :  "))

while True :
    if guess == number :
        break
    else :
        guess = int(input("NOPE ... !!! Try Again with a different number now :  "))
print("You are RIGHT Mate ...!!! I was thinking about" , number)
