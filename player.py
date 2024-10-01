###
# This file is for all the settings of the player
# Last Edited : 01.10.2024
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


# Function for having the player in the game and the rotation of the images
def draw_player(screen, player_images, player_x, player_y, current_image_index, direction):

    if player_images:
        current_image = player_images[current_image_index]

        # Flip image for the left direction
        if direction == 'left':
            # Flip horizontally
            current_image = pygame.transform.flip(current_image, True, False)

        # Rotate the image for up and down directions
        if direction == 'up':
            current_image = pygame.transform.rotate(current_image, 90)
        elif direction == 'down':
            current_image = pygame.transform.rotate(current_image, -90)

        # Draw the image
        screen.blit(current_image, (player_x, player_y))


# Player movements with the direction
def player_movements(pressed, player_x, player_y, direction):

    moving = False

    # Direction UP
    if pressed[pygame.K_UP]:
        player_y -= 5
        direction = 'up'
        moving = True

    # Direction Down
    elif pressed[pygame.K_DOWN]:
        player_y += 5
        direction = 'down'
        moving = True

    # Direction Right
    elif pressed[pygame.K_RIGHT]:
        player_x += 5
        direction = 'right'
        moving = True

    # Direction Left
    elif pressed[pygame.K_LEFT]:
        player_x -= 5
        direction = 'left'
        moving = True

    return player_x, player_y, direction, moving


# Animating the player with the images
def player_animation(screen, player_images, player_x, player_y, current_image_index, frame_count, frame_limit, direction):

    # Increment the frame count
    frame_count += 1

    if frame_count >= frame_limit:
        current_image_index = (current_image_index + 1) % len(player_images)
        frame_count = 0

    # Draw the player image with the current direction
    draw_player(screen, player_images, player_x, player_y, current_image_index, direction)
    return current_image_index, frame_count