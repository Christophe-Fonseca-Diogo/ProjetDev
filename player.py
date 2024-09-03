import pygame
import sys

import pygame

def load_player_images():
    player_images = []
    for i in range(1, 4):
        image = pygame.image.load(f'Assets/Player_Model/Player_{i}.png')
        player_images.append(image)
    return player_images

def draw_player(screen, player_images, window_width, window_height, current_image_index):
    if player_images:
        current_image = player_images[current_image_index]
        screen.blit(current_image,
                     (window_width // 2 - current_image.get_width() // 2,
                      window_height // 2 - current_image.get_height() // 2))