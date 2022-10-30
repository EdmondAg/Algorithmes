import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = 31, 4, 0, 17
# game loop
while True:

    movement = ""

    if initial_ty > light_y:
        movement = "N"
    if initial_ty < light_y:
        movement = "S"
    if initial_tx > light_x:
        movement = movement + "W"
    if initial_tx < light_x:
        movement = movement + "E"

    print(movement)
