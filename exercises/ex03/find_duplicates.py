"""Finding duplicate letters in a word."""

__author__ = "730527166"

word: str = input("Enter a word: ")
i: int = 0
check: int = 0
j: int = 0
n: int = 0
while n <= len(word) - 1:
    j = n
    i = n
    while i < len(word) - 1:
        if word[j] == word[i + 1]:
            check = check + 1
        i = i + 1
    n = n + 1
    
if check > 0: 
    print("True")
else: 
    print("False")