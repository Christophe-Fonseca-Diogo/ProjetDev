###
# This file is for the board
# Last Edited : 06.09.2024
# Made by Christophe & Zachary
# SI-C3A
###
import pygame

from dependencies import *
pygame.init()


#0 = Nothing
#1 = Wall
#2-5 Veggies
#6-9 Ghosts
board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 6, 1, 1, 1, 1, 7, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 8, 1, 0, 0, 1, 9, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Function to draw the board
def draw_board(screen):
    case_size = 45
    widht = (800 - (len(board[0]) * case_size)) // 2
    height = (800 - (len(board) * case_size)) // 2

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
    scaled_coin_size = (25, 25)
    coin_image = pygame.transform.scale(coin_image, scaled_coin_size)

    # Draw the maze on the screen
    for row in range(len(board)):
        for col in range(len(board[row])):
            # Draw the wall
            if board[row][col] == 1:
                pygame.draw.rect(screen, blue,
                                 (widht + col * case_size, height + row * case_size,
                                  case_size, case_size))
            # Draw the black rectangle for the path
            elif board[row][col] == 0:
                pygame.draw.rect(screen, black,
                                 (widht + col * case_size, height + row * case_size,
                                  case_size, case_size))

                # Calculate the position to center the coin
                coin_x = widht + col * case_size + (case_size - scaled_coin_size[0]) // 2
                coin_y = height + row * case_size + (case_size - scaled_coin_size[1]) // 2

                # Draw the coin image
                screen.blit(coin_image, (coin_x, coin_y))

            # Veggie 1 (Carrot)
            elif board[row][col] == 2:
                screen.blit(carrot_image, (widht + col * case_size, height + row * case_size))

            # Veggie 2 (Eggplant)
            elif board[row][col] == 3:
                screen.blit(eggplant_image, (widht + col * case_size, height + row * case_size))

            # Veggie 3 (Onion)
            elif board[row][col] == 4:
                screen.blit(onion_image, (widht + col * case_size, height + row * case_size))

            # Veggie 4 (Pepper)
            elif board[row][col] == 5:
                screen.blit(pepper_image, (widht + col * case_size, height + row * case_size))

            # Blue Ghost
            elif board[row][col] == 6:
                screen.blit(blue_ghost_image, (widht + col * case_size, height + row * case_size))

            # Orange Ghost
            elif board[row][col] == 7:
                screen.blit(orange_ghost_image, (widht + col * case_size, height + row * case_size))

            # Pink Ghost
            elif board[row][col] == 8:
                screen.blit(pink_ghost_image, (widht + col * case_size, height + row * case_size))

            # Red Ghost
            elif board[row][col] == 9:
                screen.blit(red_ghost_image, (widht + col * case_size, height + row * case_size))
