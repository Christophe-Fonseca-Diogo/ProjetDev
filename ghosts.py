###
# This file is for all the settings of the ghosts
# Last Edited : 26.09.2024
# Made by Christophe & Zachary
# SI-C3A
###

import random

# Movement for all ghosts
def ghosts_movements(ghost_x,ghost_y):
    # Down, Right, Left, Up
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # Choose a random direction
    direction_x, direction_y = random.choice(directions)

    # Calculate new position
    new_x = ghost_x + direction_x
    new_y = ghost_y + direction_y

    return new_x, new_y
