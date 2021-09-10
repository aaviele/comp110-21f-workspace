"""Finding duplicate letters in a word."""

__author__ = "730322189"

word: str =  input("Enter a word: ")
counter_iterations: int = 0
counter_dups: int = 0

while counter_iterations < len(word):
    counter_comp: int = counter_iterations + 1
    while counter_comp < len(word):
        if word[counter_iterations] == word[counter_comp]:
            counter_dups = counter_dups + 1
        counter_comp = counter_comp + 1
    counter_iterations = counter_iterations + 1

print("Found Duplicate: " + str(counter_dups > 0))