"""numeric operators exercise"""

__author__ : str = "730527166"

left_hand_side : int = int(input("Left-hand side: "))
right_hand_side : int= int(input("Right-hand side: "))

exponent = left_hand_side ** right_hand_side 
print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(exponent))

division = left_hand_side / right_hand_side 
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(division))

int_division = left_hand_side // right_hand_side
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(int_division))

mod = left_hand_side % right_hand_side
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(mod))

