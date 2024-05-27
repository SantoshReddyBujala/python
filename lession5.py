import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playAgain = True

while playAgain:
    playerChoice = input(
        "\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("You must Ener 1, 2, 3 ...")

    computerChoice = random.choice("123")
    computer = int(computerChoice)
    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")
    playAgain = input("\n Play Again? \n Y for Yes or \n Q for Quit \n\n")

    if playAgain.lower() == 'y':
        continue
    else:
        print("\n 🎉🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        break
sys.exit("Bye! 👋")
