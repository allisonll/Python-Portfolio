#Allison Liao
#11/8/24
#Number Guesser

#Initialize
import random

#Function

#This function allows us to guess a number
#and sees if it matches with another randomly generated number from 1-10
#x = random Interger
#ans = Interger

def numberGuesser():
    print("Welcome to the Number Generator!")
    print("Play three rounds to test your luck! Get points if you guess correctly.")
    print("6 points will get you 1 cookie!")

    for i in range(3):
        x = random.randint(1,10)
        y = 0
        ans = int(input("Please Enter A Number 1-10"))
        if ans == x:
            y = y + 2
            print("You guessed the number!")
            print("You get " + str(y) + " points!")
            y = y
        else:
            print("You didn't guess the number, Try Again.")
            print("The correct number was " + str(x) + ".")
            print("You get no points.")

    print("You have " + str(y) + " points.")

#Main
numberGuesser()



