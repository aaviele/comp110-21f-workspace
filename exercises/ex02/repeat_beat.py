"""Repeating a beat in a loop."""

__author__ = "730322189"

beat: str = input("What beat do you want to repeat? ")
num: int = int(input("How many times do you want to repeat? "))
i: int = 0
print_this: str = ""

if num <= 0:
    print("No beat...")

while i < num - 1:
    print_this = beat + " " + print_this
    i = i + 1

print_this = print_this + beat

print(print_this)