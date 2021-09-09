"""Finding duplicate letters in a word."""

__author__ = "730322189"

word: str =  input("Enter a word: ")
i: int = 0
k: int = 0

while i < len(word):
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            k = k + 1
        j = j + 1
    i = i + 1

print("Found Duplicate: " + str(k > 0))