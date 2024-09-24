###
# This file is for all the settings of the player
# Last Edited : 06.09.2024
# Made by Christophe & Zachary
# SI-C3A
###

import pygame
# Load all the images for the game
def load_player_images(width, height):
    player_images = []
    for i in range(1, 5):
        image = pygame.image.load(f'Assets/Player_Model/Player_{i}.png')
        # Scale the image of the player
        scaled_image = pygame.transform.scale(image, (width, height))
        player_images.append(scaled_image)
    return player_images

# Function for placing the player in the game
def draw_player(screen, player_images, player_x, player_y, current_image_index):
    if player_images:
        current_image = player_images[current_image_index]
        screen.blit(current_image, (player_x, player_y))

def player_movements(pressed, player_x, player_y):
    if pressed[pygame.K_UP]:
        player_y -= 5
    if pressed[pygame.K_DOWN]:
        player_y += 5
    if pressed[pygame.K_RIGHT]:
        player_x += 5
    if pressed[pygame.K_LEFT]:
        player_x -= 5

    return player_x, player_y
