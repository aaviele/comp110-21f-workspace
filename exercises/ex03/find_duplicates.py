"""Finding duplicate letters in a word."""

__author__ = "730322189"

word: str =  input("Enter a word: ")
i: int = 0
j: int = 0
k: int = 0

while i < len(word):
    i = i + 1
    while j > i + 1 and j < len(word):
        if word[i] == word[j] and word[i] != "":
            k = k + 1
        j = j + 1

if k < 1:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")

