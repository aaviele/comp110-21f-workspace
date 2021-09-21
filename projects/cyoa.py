"""create your own adventure project"""

__author__ = "730322189"

from random import randint

points: int = 0
player: str = ""
restart: bool = True
NAMED_CONSTANT: str = '\U0001F44B'

def main() -> None:
    global points
    global player
    global restart
    greet()
    while restart == True:
        enter_the_game: str = input("Would you like to guess heads, guess tails, or end the game? Enter H for heads. Enter T for tails. Enter E for end game. ")
        if enter_the_game == "H":
            heads_guess()
        if enter_the_game == "T":
            tails_guess()
        if enter_the_game  ==  "E":
            print(f"You have earned {points} adventure point(s).")
            print(f"Goodbye {player}!")
            restart = False

def heads_guess():
    global points
    global restart
    num: int = int(input("Guess how many heads out of 10 coinflips: "))
    correct_heads: int = randint(0, 10)
    if num == correct_heads:
        points = points + 1
    print(f"The correct answer was {correct_heads}.")
    print(f"You have {points} adventure point(s).")
    restart = bool(input("Do you want to continue playing? Enter True for yes. Enter False for no. "))

def tails_guess():
    global points
    global restart
    num: int = int(input("Guess how many tails out of 10 coinflips: "))
    correct_tails: int = randint(0, 10)
    if num == correct_tails:
        points = points + 1
    print(f"The correct answer was {correct_tails}.")
    print(f"You have {points} adventure point(s).")
    restart = bool(input("Do you want to continue playing? Enter True for yes. Enter False for no. "))

def greet():
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}! {NAMED_CONSTANT} In this game, you  will try to guess the number of heads or tails out of 10 coinflips. For each correct guess, you will earn one adventure point.")

if __name__ == "__main__":
    main()