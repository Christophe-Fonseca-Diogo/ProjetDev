###
# This file is for the game
# Last Edited : 26.09.2024
# Made by Christophe & Zachary
# SI-C3A
###

import player
from ghosts import *
from board import draw_board
from dependencies import *

player_x = 377
player_y = 450

# Music for the game
def game_music():
    pygame.mixer.init()
    music = pygame.mixer.Sound("Assets/Sounds/Game.mp3")
    # -1 for infinite loop
    music.play(loops=-1)


def game_title():
    # Title settings
    title_font = pygame.font.Font('Assets/PAC-FONT.TTF', 80)
    title_text = title_font.render('PAC-MAN', True, yellow, (0, 0, 0))
    title_text_rect = title_text.get_rect()

    # set the center of the rectangular object.
    title_text_rect.center = (window_width // 2, window_height // 12)
    # show in the screen
    screen.blit(title_text, title_text_rect)


# Window settings for the game
def game_settings():
    global player_images, character
    pygame.init()
    global screen, window_width, window_height
    # Set up the window dimensions
    window_width = 800
    window_height = 900

    # Create the screen object
    screen = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption("GAME PAC-MAN")

    # Set the icon of the window
    game_icon = pygame.image.load('Icons/Joystick.png')

    pygame.display.set_icon(game_icon)
    player_images = player.load_player_images(40, 40)


# Loop for the game
def game_loop():
    global player_x, player_y, tick

    # Initialize the image index
    current_image_index = 0
    # Initialize the frame count
    frame_count = 0
    # Set the frame limit
    frame_limit = 5
    tick = 0
    last_direction = 'right'

    # Load ghosts images and create ghost instances
    ghost_images = load_ghost_images(case_size)  # Load ghost images
    ghosts = create_ghosts(board, ghost_images)  # Create ghost instances

    running = True
    # Background music for the game
    game_music()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill(black)
        # Draw game title and the board
        game_title()
        draw_board(screen)

        # Get player movements and direction
        player_x, player_y, last_direction, moving = player.player_movements(pygame.key.get_pressed(), player_x,
                                                                             player_y, last_direction)
        # Update the player's animation based on position
        current_image_index, frame_count = player.player_animation(screen, player_images, player_x, player_y,current_image_index,
                                                                   frame_count, frame_limit, last_direction, tick)
        # Example initialization:
        # Place the player in its starting position (presumably in the board array)

        if tick == 15:
            # Move the ghosts
            tick = 0
            move_ghosts(ghosts)

        tick += 1

        # Draw the ghosts on the screen
        width = (800 - (len(board[0]) * case_size)) // 2
        height = (950 - (len(board) * case_size)) // 2
        draw_ghosts(screen, ghosts, width, height)  # Draw ghosts

        pygame.display.update()


if __name__ == "__main__":
    # Main windows settings
    game_settings()
    # Using the loop for the game
    game_loop()
