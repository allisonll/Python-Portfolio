#Allison Liao
#1/29
#Slot Machine

#Initalize
symbols = [ "7", "✵", "✶", "✦", "✧", "★", "☆"]
import random
import time

#Function
#This function allows you to play a slot machine and see if you win or lose.
def slotMachine():
    global credits
    print("Welcome to the Star Slot Machine!")
    print("You have 100 credits to start. Each spin is 10 credits.")
    print("To start the slot machine, either pull the lever to spin OR quit.")
    print(" ")
    credits = 100

    while True:
        if credits < 10:
            print("You don't have enough credits to spin.")
            print("Would you like to buy more credits?")
            buyCredits = input("Yes(Y) or No(N)")
            buyCredits = buyCredits.lower()
            if buyCredits == "y":
                print("You get 10 more credits")
                print(" ")
                credits = credits + 10
                credits = credits
            else:
                print("You cannot play.")
                break

        action = input("Would you like to spin (S) or quit (Q)?")
        action = action.lower()

        credits = credits - 10
        if action == "s":
            print("Get ready for the slot machine to spin!")
            time.sleep(2)
            print("Spinning..")
            time.sleep(2)
            print("Spinning..")
            print(" ")
            slot1 = random.choices(symbols, weights = [1, 3, 2, 3, 2, 3, 2], k = 1)
            slot2 = random.choices(symbols, weights = [1, 2, 3, 2, 3, 2, 3], k = 1)
            slot3 = random.choices(symbols, weights = [1, 3, 2, 3, 2, 3, 2], k = 1)
            print("Current Slots: " + str(slot1) + str(slot2) + str(slot3))
            if slot1 == slot2 == slot3 and slot1 == "7":
                print("You got a Jackpot!!")
                print("This means you get 100 credits!")
                credits = credits + 100
                print("Credits: " + str(credits))
                credits = credits
                print(" ")

            elif slot1 == slot2 == slot3 and slot1 != "7":
                print("You won!")
                print("You get 10 credits")
                credits = credits + 10
                print("Credits: " + str(credits))
                credits = credits
                print(" ")
            elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                print("You won with a double!")
                print("You get 5 credits")
                credits = credits + 10
                print("Credits: " + str(credits))
                credits == credits
                print(" ")
            else:
                print("You didn't win :(")
                print("You don't earn any credits.")
                print("Credits: " + str(credits))
                credits = credits
                print(" ")

        elif action == "q":
            print("Thanks for playing!")
            break


        else:
            print("You didn't enter a correct action. Try again.")
            credits = credits + 10
            credits = credits
            print(" ")

#Main
slotMachine()
