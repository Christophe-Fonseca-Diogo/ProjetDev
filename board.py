###
# This file is for the board
# Last Edited : 26.09.2024
# Made by Christophe & Zachary
# SI-C3A
###

import pygame
from dependencies import *
pygame.init()

# 0 = Nothing
# 1 = Wall
# 2-5 Veggies
# 6-9 Ghosts
# 10 Player

board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 3, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 6, 0, 0, 0, 0, 0, 7, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 8, 0, 0, 0, 0, 0, 9, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# Function to draw the board
def draw_board(screen):
    case_size = 45
    width = (800 - (len(board[0]) * case_size)) // 2
    height = (950 - (len(board) * case_size)) // 2

    # Load and scale veggies images
    carrot_image = pygame.image.load('Assets/Veggies/carrot.png')
    carrot_image = pygame.transform.scale(carrot_image, (case_size, case_size))

    eggplant_image = pygame.image.load('Assets/Veggies/eggplant.png')
    eggplant_image = pygame.transform.scale(eggplant_image, (case_size, case_size))

    onion_image = pygame.image.load('Assets/Veggies/onion.png')
    onion_image = pygame.transform.scale(onion_image, (case_size, case_size))

    pepper_image = pygame.image.load('Assets/Veggies/pepper.png')
    pepper_image = pygame.transform.scale(pepper_image, (case_size, case_size))

    # Load and scale ghosts images
    blue_ghost_image = pygame.image.load('Assets/Ghosts/blue.png')
    blue_ghost_image = pygame.transform.scale(blue_ghost_image, (case_size, case_size))

    orange_ghost_image = pygame.image.load('Assets/Ghosts/orange.png')
    orange_ghost_image = pygame.transform.scale(orange_ghost_image, (case_size, case_size))

    pink_ghost_image = pygame.image.load('Assets/Ghosts/pink.png')
    pink_ghost_image = pygame.transform.scale(pink_ghost_image, (case_size, case_size))

    red_ghost_image = pygame.image.load('Assets/Ghosts/red.png')
    red_ghost_image = pygame.transform.scale(red_ghost_image, (case_size, case_size))

    # Load and scale the coin image
    coin_image = pygame.image.load('Assets/Coin.png')
    scaled_coin_size = (20, 20)
    coin_image = pygame.transform.scale(coin_image, scaled_coin_size)

    # Draw the board on the screen
    for row in range(len(board)):
        for col in range(len(board[row])):

            # Draw the wall
            if board[row][col] == 1:
                pygame.draw.rect(screen, blue,
                                 (width + col * case_size, height + row * case_size,
                                  case_size, case_size))

            # Draw the black rectangle for the path
            elif board[row][col] == 0:
                pygame.draw.rect(screen, black,
                                 (width + col * case_size, height + row * case_size,
                                  case_size, case_size))

                # Calculate the position to center the coin
                coin_x = width + col * case_size + (case_size - scaled_coin_size[0]) // 2
                coin_y = height + row * case_size + (case_size - scaled_coin_size[1]) // 2

                # Draw the coin image
                screen.blit(coin_image, (coin_x, coin_y))

            # Draw all the objects in map
            elif 2 <= board[row][col] <= 9:
                obj_list = { 2: eggplant_image, 3: carrot_image, 4: onion_image, 5: pepper_image,
                             6: blue_ghost_image, 7: orange_ghost_image, 8: pink_ghost_image, 9: red_ghost_image}
                screen.blit(obj_list[board[row][col]], (width + col * case_size, height + row * case_size))
