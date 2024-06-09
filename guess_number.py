import sys
import random


def guess_number(name="PlayerOne"):
    game_count = 0
    player_win = 0

    def play_pgn():
        nonlocal name
        nonlocal player_win

        playerChoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")

        if (playerChoice not in ["1", "2", "3"]):
            print(f"{name} please enter 1, 2, 3 ...")
            return play_pgn()

        computerChoice = random.choice("123")
        print(f"\n{name}, you chose {playerChoice}")
        print(f"I was thing about the number {computerChoice}.\n")

        player = int(playerChoice)
        computer = int(computerChoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_win
            if player == computer:
                player_win += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 😔"
        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\n Game count: {game_count}")
        print(f"\n {name}'s wins: {player_win}")
        print(f"\n Your winning percentage: {player_win / game_count:.2%}")

        playAgain = (f"\nPlay again, {name}?")
        while True:
            playAgain = input("\n Play Again? \n Y for Yes or \n Q for Quit\n")
            if playAgain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playAgain.lower() == 'y':
            return play_pgn()
        else:
            print("\n 🎉🎉🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")
    return play_pgn


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provide a personalized game experiance"
    )

    parser.add_argument(
        "-n", "--name", metavar="Name", required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()
    g_n = guess_number(args.name)
    g_n()
