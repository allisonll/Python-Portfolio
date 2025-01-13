#Allison Liao
#1/7/25
#Rock Paper Scissors

#Initialize
import random

#Functions

#This function allows for kindergardeners to play rock paper scissors easily.
def rpsGame():
    global pmove
    global cmove
    global pscore
    global cscore
    global play
    global win
    global lose
    global tie

    win = 0
    lose = 0
    tie = 0

    cscore = 0
    pscore = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("What is your first move?")

    while True:
        pmove = input("Rock, Paper, or Scissors? (R, P, S)")
        pmove = pmove.upper()


        cmove = random.randint(1,3)

        if cmove == 1:
            cmove = "R"
            print("The computer's move is Rock!")
        elif cmove == 2:
            cmove = "P"
            print("The computer's move is Paper!")
        else:
            cmove = "S"
            print("The computer's move is Scissors!")



        if cmove == "R" and pmove == "S":
            print("The computer wins!")
            cscore = cscore + 1
            win = win
            lose = lose + 1
            tie = tie
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif cmove == "P" and pmove == "R":
            print("The computer wins!")
            cscore = cscore + 1
            win = win
            lose = lose + 1
            tie = tie
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif cmove == "S" and pmove == "P":
            print("The computer wins!")
            cscore = cscore + 1
            win = win
            lose = lose + 1
            tie = tie
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif pmove == "R" and cmove == "S":
            print("You win!")
            pscore = pscore + 1
            win = win + 1
            lose = lose
            tie = tie
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif pmove == "P" and cmove == "R":
            print("You win!")
            pscore = pscore + 1
            win = win + 1
            lose = lose
            tie = tie
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif pmove == "S" and cmove == "P":
            print("You win!")
            pscore = pscore + 1
            win = win + 1
            lose = lose
            tie = tie
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif pmove == "R" and cmove == "R":
            print("There is a tie! There is no winner.")
            cscore = cscore + 0
            pscore = pscore + 0
            win = win
            lose = lose
            tie = tie + 1
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif pmove == "P" and cmove == "P":
            print("There is a tie! There is no winner.")
            cscore = cscore + 0
            pscore = pscore + 0
            win = win
            lose = lose
            tie = tie + 1
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()

        elif pmove == "S" and cmove == "S":
            print("There is a tie! There is no winner.")
            cscore = cscore + 0
            pscore = pscore + 0
            win = win
            lose = lose
            tie = tie + 1
            print("The score to the left is your score.")
            print("The score is: " + str(pscore) + " to " + str(cscore))
            print(" ")
            print("Statistics:")
            print("Wins = " + str(win))
            print("Lossses = " + str(lose))
            print("Ties = " + str(tie))
            print(" ")
            print("Would you like to keep playing?")
            play = input("Yes or No? (Y or N)")
            play = play.upper()


        if play == "N":
            print("Thanks for playing!")
            print("See you next time!")
            break

#Main
rpsGame()

