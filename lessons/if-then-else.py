"""Practice with if-then-else statements."""

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")

if choice > 75:
    print("C")
else:
    if choice >= 50:
        print("D")