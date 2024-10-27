###
# This file is for all the settings of the ghosts
# Last Edited : 26.09.2024
# Made by Christophe & Zachary
# SI-C3A
###

import pygame
import random
from board import board


# Load ghost images into a list
def load_ghost_images(case_size):
    ghost_images = []
    for ghost_index in range(4):  # Assuming there are 4 ghosts (indices: 6-9)
        image = pygame.image.load(f'Assets/Ghosts/Ghost{ghost_index + 1}.png')
        scaled_image = pygame.transform.scale(image, (case_size, case_size))
        ghost_images.append(scaled_image)

    return ghost_images

# Function to create a list of ghosts from the board data
def create_ghosts(board, ghost_images):
    ghosts = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if 6 <= board[row][col] <= 9:  # Check for ghost positions
                ghosts.append([col, row, ghost_images[board[row][col] - 6]])  # [x, y, image]
    return ghosts



# Move the ghosts
def move_ghosts(ghosts):
    for ghost in ghosts:
        direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  # Down, Up, Left, Right
        new_x = ghost[0] + direction[0]
        new_y = ghost[1] + direction[1]

        # Check new position is valid (within bounds and not a wall)
        if 0 <= new_x < len(board[0]) and 0 <= new_y < len(board):
            if board[new_y][new_x] != 1:  # Not a wall
                ghost[0], ghost[1] = new_x, new_y  # Update position


# Draw the ghosts at their current positions
def draw_ghosts(screen, ghosts, offset_x, offset_y):
    for ghost in ghosts:
        screen.blit(ghost[2], (offset_x + ghost[0] * 45, offset_y + ghost[1] * 45))  # Ghost[0]: x, Ghost[1]: y, Ghost[2]: image
