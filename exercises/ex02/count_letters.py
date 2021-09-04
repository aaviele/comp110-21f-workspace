"""Counting letters in a string."""

__author__ = "730322189"


letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
i: int = 0
print_this: int = 0

while i < len(word): 
    if letter == word[i]:
        print_this = print_this + 1
        
    i = i + 1

if print_this <= 0:
    print("Count: 0")
 
print(print_this)