###
# This file is for all the settings of the player
# Last Edited : 03.09.2024
# Made by Christophe & Zachary
# SI-C3A
###

import pygame


def load_player_images(width, height):
    player_images = []
    for i in range(1, 4):
        # Load the image
        image = pygame.image.load(f'Assets/Player_Model/Player_{i}.png')
        # Scale the image
        scaled_image = pygame.transform.scale(image, (width, height))
        player_images.append(scaled_image)
    return player_images


def draw_player(screen, player_images, window_width, window_height, current_image_index):
    if player_images:
        current_image = player_images[current_image_index]
        screen.blit(current_image,
                     (window_width // 2 - current_image.get_width() // 2,
                      window_height // 2 - current_image.get_height() // 2))
