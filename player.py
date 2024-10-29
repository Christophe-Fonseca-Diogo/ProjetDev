###
# This file is for all the settings of the player
# Last Edited : 29.10.2024
# Made by Christophe & Zachary
# SI-C3A
###

import pygame
from board import board
from dependencies import *

# Music for the coin sound
def coin_sound():
    pygame.mixer.init()
    coin_pickup_sound = pygame.mixer.Sound("Assets/Sounds/coin_sound.mp3")
    coin_pickup_sound.set_volume(0.1)
    coin_pickup_sound.play()

# Variable for the lives of the player
lives = 3

# Function to load the images of the player
def load_player_images(case_size):
    player_images = []
    for i in range(1, 5):
        image = pygame.image.load(f'Assets/Player_Model/Player_{i}.png')
        # Scale the image of the player
        scaled_image = pygame.transform.scale(image, (case_size, case_size))
        player_images.append(scaled_image)

    return player_images

# Function for having the player in the game and the rotation of the images
def draw_player(screen, player_images, player_x, player_y, current_image_index, direction, offset_x, offset_y, case_size):
    if player_images:
        current_image = player_images[current_image_index]

        # Flip image for the left direction
        if direction == 'left':
            current_image = pygame.transform.flip(current_image, True, False)

        # Rotate the image for up and down directions
        if direction == 'up':
            current_image = pygame.transform.rotate(current_image, 90)
        elif direction == 'down':
            current_image = pygame.transform.rotate(current_image, -90)

        # Calculate draw position based on case size to center it
        player_x_position = offset_x + player_x - (current_image.get_width() // 2) + (case_size // 2)
        player_y_position = offset_y + player_y - (current_image.get_height() // 2) + (case_size // 2)

        # Draw the image
        screen.blit(current_image, (player_x_position, player_y_position))

# Function for the coins
def update_board_coins(board, player_grid_x, player_grid_y, score):
    # Check for coin collection at the new position
    if board[player_grid_y][player_grid_x] == 0:
        score += 100
        coin_sound()
        # Change coin to collected state (12)
        board[player_grid_y][player_grid_x] = 12

    # Clean previous position (only after checking the coin)
    for row in range(len(board)):
        for col in range(len(board[row])):
            # Check for the player's previous position
            if board[row][col] == 10:
                # Set previous position to empty path
                board[row][col] = 11

    # Set new position
    board[player_grid_y][player_grid_x] = 10

    return score

# Player movements with the direction
def player_movements(pressed, player_grid_x, player_grid_y, direction, frame_count):
    moving = False

    # Frames for the player
    move_threshold = 10

    # Direction UP
    if pressed[pygame.K_UP]:
        if frame_count % move_threshold == 0:
            if player_grid_y > 0 and board[player_grid_y - 1][player_grid_x] != 1:
                # Move up
                player_grid_y -= 1
                direction = 'up'
                moving = True

    # Direction Down
    elif pressed[pygame.K_DOWN]:
        if frame_count % move_threshold == 0:
            if player_grid_y < len(board) - 1 and board[player_grid_y + 1][player_grid_x] != 1:
                # Move down
                player_grid_y += 1
                direction = 'down'
                moving = True

    # Direction Right
    elif pressed[pygame.K_RIGHT]:
        if frame_count % move_threshold == 0:
            if player_grid_x < len(board[0]) - 1 and board[player_grid_y][player_grid_x + 1] != 1:
                # Move right
                player_grid_x += 1
                direction = 'right'
                moving = True

    # Direction Left
    elif pressed[pygame.K_LEFT]:
        if frame_count % move_threshold == 0:
            if player_grid_x > 0 and board[player_grid_y][player_grid_x - 1] != 1:
                # Move left
                player_grid_x -= 1
                direction = 'left'
                moving = True

    return player_grid_x, player_grid_y, direction, moving

# Animating the player with the images
def player_animation(screen, player_images, player_x, player_y, current_image_index, frame_count, frame_limit, direction, tick, offset_x, offset_y):

    # Increment the frame count
    frame_count += 1

    if frame_count >= frame_limit and tick == 1:
        current_image_index = (current_image_index + 1) % len(player_images)
        frame_count = 0

    # Draw the player image with the current direction
    draw_player(screen, player_images, player_x, player_y, current_image_index, direction, offset_x, offset_y, case_size)

    return current_image_index, frame_count

# Function to check collision with ghosts
def check_collision(player_x, player_y, ghosts):
    player_rect = pygame.Rect(player_x, player_y, case_size, case_size)
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost[0] * case_size, ghost[1] * case_size, case_size, case_size)
        if player_rect.colliderect(ghost_rect):
            return True
    return False
