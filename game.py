# This file is for the game
# Last Edited : 26.09.2024
# Made by Christophe & Zachary
# SI-C3A
###
import board
import player
from ghosts import *
from board import draw_board
from dependencies import *

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
    player_images = player.load_player_images(case_size)


# Loop for the game
def game_loop():
    global tick

    # Initialize player's grid position
    player_grid_x = player.starting_col
    player_grid_y = player.starting_row

    current_image_index = 0
    frame_count = 0
    frame_limit = 5
    tick = 0
    last_direction = 'right'

    ghost_images = load_ghost_images(player.case_size)
    ghosts = create_ghosts(board, ghost_images)

    running = True
    game_music()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)
        game_title()

        if tick == 15:
            tick = 0
            move_ghosts(ghosts)

        tick += 1

        width = (800 - (len(board[0]) * player.case_size)) // 2
        height = (950 - (len(board) * player.case_size)) // 2

        # Draw the board
        draw_board(screen)

        # Draw ghosts
        draw_ghosts(screen, ghosts, width, height)

        # Get player movements and direction
        player_grid_x, player_grid_y, last_direction, moving = player.player_movements(
            pygame.key.get_pressed(), player_grid_x, player_grid_y, last_direction, frame_count)

        # Update the board with the player's grid position
        player.update_board(board, player_grid_x, player_grid_y)

        # Update the player's animation based on position
        current_image_index, frame_count = player.player_animation(screen, player_images,
            player_grid_x * player.case_size, player_grid_y * player.case_size,
            current_image_index, frame_count, frame_limit, last_direction, tick, width, height)

        # Update the display
        pygame.display.flip()





if __name__ == "__main__":
    # Main windows settings
    game_settings()
    # Using the loop for the game
    game_loop()
