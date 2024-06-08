import sys
import random
from enum import Enum
import argparse


def rps(name="PlayerOne"):
    game_count = 0
    player_win = 0
    python_win = 0

    def play_rps():
        nonlocal name
        nonlocal player_win
        nonlocal python_win

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerChoice = input(
            f"\n{name}, please enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

        if (playerChoice not in ["1", "2", "3"]):
            print(f"{name} please enter 1, 2, 3 ...")
            return play_rps()

        player = int(playerChoice)

        computerChoice = random.choice("123")
        computer = int(computerChoice)
        print(f"\n{name}, you chose {
              str(RPS(player)).replace("RPS.", "").title()}.")
        print(f"Python chose {
              str(RPS(computer)).replace("RPS.", "").title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_win
            nonlocal python_win
            if player == 1 and computer == 3:
                player_win += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_win += 1
                return f"🎉 {name}, you win!"
            elif player == 3 and computer == 2:
                player_win += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_win += 1
                return "🐍 Python wins!"
        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\n Game count: {game_count}")
        print(f"\n {name}'s wins: {player_win}")
        print(f"\n Python wins: {python_win}")
        print(f"\n Play Again {name}?")
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
            sys.exit(f"Bye {name}! 👋")
    return play_rps


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Provide a personalized game experiance"
    )

    parser.add_argument(
        "-n", "--name", metavar="Name", required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()
    r_p_s = rps(args.name)
    r_p_s()
