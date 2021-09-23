"""Create your own adventure project."""

from random import randint

__author__ = "730322189"

NAMED_CONSTANT: str = '\U0001F44B'


points: int
player: str
restart: bool


def main() -> None:
    """This connects all the other functions."""
    global points
    global player
    global restart
    points = 0
    player = ""
    restart = True
    greet()
    while restart:
        enter_the_game: str = input("Would you like to guess heads, guess tails, or end the game? Enter H for heads. Enter T for tails. Enter E for end game. ")
        if enter_the_game == "H":
            heads_guess()
            menu()
        if enter_the_game == "T":
            points = tails_guess(points, player)
            print(f"You have {points} adventure point(s).")
            menu()
        if enter_the_game == "E":
            print(f"You have earned {points} adventure point(s).")
            print(f"Goodbye, {player}!")
            restart = False


def heads_guess() -> None:
    """Checks if guess for number of heads is correct and gives one point if so."""
    global points
    global restart
    global player
    num: int = int(input(f"{player}, guess how many heads out of 10 coinflips: "))
    correct_heads: int = randint(0, 10)
    if num == correct_heads:
        points = points + 1
    print(f"The correct answer was {correct_heads}.")
    print(f"You have {points} adventure point(s).")


def tails_guess(points: int, player: str) -> int:
    """Checks if guess for number of tails is correct and gives one point if so."""
    num: int = int(input(f"{player}, guess how many tails out of 10 coinflips: "))
    correct_tails: int = randint(0, 10)
    if num == correct_tails:
        points = points + 1
    print(f"The correct answer was {correct_tails}.")
    return points


def greet() -> None:
    """Greets player and gives game instructions!"""
    global player
    player = input("What is your name? ")
    print(f"Welcome, {player}! {NAMED_CONSTANT} In this game, you  will try to guess the number of heads or tails out of 10 coinflips. For each correct guess, you will earn one adventure point.")


def menu() -> None:
    """Asks player if they want to continue playing and continues or ends the game accordingly."""
    global restart
    global player
    global points
    continue_game: str = input(f"{player}, do you want to continue playing? Enter Y for yes. Enter N for no. ")
    if continue_game == "Y":
        restart = True
    if continue_game == "N":
        print(f"You have earned {points} adventure point(s).")
        print(f"Goodbye, {player}!")
        restart = False


if __name__ == "__main__":
    main()