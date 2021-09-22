"""create your own adventure project."""

__author__ = "730322189"

NAMED_CONSTANT: str = '\U0001F44B'


from random import randint


points: int
player: str
restart: bool


def main() -> None:
    points = 0
    player = ""
    restart = True
    greet()
    while restart == True:
        enter_the_game: str = input("Would you like to guess heads, guess tails, or end the game? Enter H for heads. Enter T for tails. Enter E for end game. ")
        if enter_the_game == "H":
            num: int = int(input("Guess how many heads out of 10 coinflips: "))
            points = heads_guess(num, points)
            print(f"You have {points} adventure point(s).")
        if enter_the_game == "T":
            num: int = int(input("Guess how many tails out of 10 coinflips: "))
            points = tails_guess(num, points)
            print(f"You have {points} adventure point(s).")
        if enter_the_game  ==  "E":
            print(f"You have earned {points} adventure point(s).")
            print(f"Goodbye!")
            restart = False


def heads_guess(num: int, points = int) -> None: 
    correct_heads: int = randint(0, 10)
    if num == correct_heads:
        points = points + 1
    print(f"The correct answer was {correct_heads}.")
    return points


def tails_guess(num: int, points: int) -> None:
    correct_tails: int = randint(0, 10)
    if num == correct_tails:
        points = points + 1
    print(f"The correct answer was {correct_tails}.")
    return points


def greet() -> None:
    player: str = input("What is your name? ")
    print(f"Welcome, {player}! {NAMED_CONSTANT} In this game, you  will try to guess the number of heads or tails out of 10 coinflips. For each correct guess, you will earn one adventure point.")


def menu() -> None:
    continue_game: str = input(f"{player}, Do you want to continue playing? Enter Y for yes. Enter N for no. ")
    if continue_game == "Y":
         restart = True
    if continue_game == "N":
        restart = False


if __name__ == "__main__":
    main()