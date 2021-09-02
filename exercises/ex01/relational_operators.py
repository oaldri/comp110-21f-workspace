"""relational operators on my own."""
__author__ = "730383481"

left_hand_side: str = input("left hand side. ")
right_hand_side: str = input("right hand side. ")

print(left_hand_side + " < " + right_hand_side + " is " + str(int(left_hand_side) < int(right_hand_side)))
print(left_hand_side + " >= " + right_hand_side + " is " + str(int(left_hand_side) >= int(right_hand_side)))
print(left_hand_side + " == " + right_hand_side + " is " + str(left_hand_side == right_hand_side))
print(left_hand_side + " != " + right_hand_side + " is " + str(left_hand_side != right_hand_side))