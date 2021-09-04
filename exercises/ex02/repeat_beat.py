"""Repeating a beat in a loop."""

__author__ = "730322189"

beat: str = input("What beat do you want to repeat? ")
num: int = int(input("How many times do you want to repeat? "))
i: int = 0
print_this: str = ""
while i < num:
    print_this = beat + " " + print_this
    i = i + 1

print(print_this)