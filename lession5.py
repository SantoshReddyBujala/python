import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_win = 0
    python_win = 0

    def play_rps():
        nonlocal player_win
        nonlocal python_win

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
        print(f"\nYou chose {str(RPS(player)).replace("RPS.", "").title()}.")
        print(f"Python chose {
              str(RPS(computer)).replace("RPS.", "").title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_win
            nonlocal python_win
            if player == 1 and computer == 3:
                player_win += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_win += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_win += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_win += 1
                return "🐍 Python wins!"
        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\n Game count: {str(game_count)}")
        print(f"\n Player wins: {str(player_win)}")
        print(f"\n Python wins: {str(python_win)}")
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
    return play_rps


r_p_s = rps()
if __name__ == "__main__":
    r_p_s()
