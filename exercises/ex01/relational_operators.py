"""relational operators exercise"""

__author__ : str = "730527166"

left_hand_side : int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

less_than = left_hand_side < right_hand_side
print(str(left_hand_side) + " < " + str(right_hand_side) + " is " + str(less_than))

atleast = left_hand_side >= right_hand_side
print(str(left_hand_side) + " >= " + str(right_hand_side) + " is " + str(atleast))

equal_to = left_hand_side == right_hand_side
print(str(left_hand_side) + " == " + str(right_hand_side) + " is " + str(equal_to))

not_equal_to = left_hand_side != right_hand_side
print(str(left_hand_side) + " != " + str(right_hand_side) + " is " + str(not_equal_to))

