"""Finding duplicate letters in a word."""

__author__ = "730322189"

word: str =  input("Enter a word: ")
i: int = 0
boolean_var: bool = False

while i < len(word):
    j: int = 0
    k: int = 0
    while j < len(word):
        if word[i] == word[j]:
            k = k + 1
        j = j + 1
        if k > 1:
            boolean_var: bool = True
    i = i + 1

print("Found Duplicate: " + str(boolean_var))