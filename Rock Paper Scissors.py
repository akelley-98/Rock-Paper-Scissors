# Program name: Rock Paper Scissors
# Author: Austin Kelley
# Date: 4/18/2022
# Summary: You play a game of rock, paper, scissors with the computer
# Variables:
#   choices: The 3 choices you have (string)
#   computer: Random choice the computer makes out of rock, paper, or scissors (string)
#   player: Input from the user (string)
#   play_again: Yes or no from user (string)

# Tells computer to make a random choice
import random

# All the code is in a while loop so if the user wants to play again, they can.
while True:
# The variables of the code.
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
# If user does not enter either rock, paper or scissors, it will loop until one of the 3 is entered.
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

# A series of if and elif statements of all the possible results of the game resulting in a Tie, a Win or a Lose.
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("It's a Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You LOSE!!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You WIN!!")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You WIN!!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You LOSE!!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You LOSE!!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You WIN!!")

# Will ask the user if they want to play again.
    play_again = input("Play again? (yes/no): ").lower()

# If yes, then the whole code will restart but if no, the computer will print "It was fun playing! BYE!!" and the code will end.
    if play_again != "yes":
        break
print("It was fun playing! BYE!!")

