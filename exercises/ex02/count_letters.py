"""Counting letters in a string."""

__author__ = "730322189"


letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
i: int = 0
printThis: int = 0

while i < len(word): 
    if letter == word[i]:
        printThis = printThis + 1
        
    i = i + 1

print(printThis)