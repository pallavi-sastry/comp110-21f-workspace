"""Repeating a beat in a loop."""

__author__ = "730527166"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeat_no: int = int(input("How many times do you want to repeat it? "))

i: int = 0
new_beat: str = beat
if repeat_no <= 0: 
    print("No beat...")
else:
    while i < (repeat_no - 1): 
        beat = new_beat + " " + beat 
        i = i + 1
    print(beat)