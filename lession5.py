import sys
import random
from enum import Enum

game_count = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        "\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    if (playerChoice not in ["1", "2", "3"]):
        print("You must Ener 1, 2, 3 ...")
        return play_rps()

    player = int(playerChoice)

    computerChoice = random.choice("123")
    computer = int(computerChoice)
    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"
    game_result = decide_winner(player, computer)

    print(game_result)
    global game_count
    game_count += 1
    print("\n Game count"+str(game_count))
    print("\n Play Again?")
    while True:
        playAgain = input("\n Play Again? \n Y for Yes or \n Q for Quit\n")
        if playAgain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playAgain.lower() == 'y':
        return play_rps()
    else:
        print("\n 🎉🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
