print("Colour Guessing Game VIBGYOR")

import random

colors = ["violet", "indigo", "black", "green","yellow", "orange", "red"]

while True :
    color = colors[random.randint(0, len(colors) -1)]
    guess = input("I am thinking about a colour..!! Can you guess it my dear friend ?   :")

    while True :
        if (color == guess.lower()) :
            break
        else :
            guess = input("Nope Friend ... !! Try again :  ")
    print("Correct..!! I was thinking about :  ", color)

    play_again = input("Wanna play again ?  or Type 'no' to quit from the game   ")
    if play_again.lower() == 'no' :
        break

print("It was fun playing with you ..!!")
