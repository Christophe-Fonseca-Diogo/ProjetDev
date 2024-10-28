# This file is for the game
# Last Edited : 28.10.2024
# Made by Christophe & Zachary
# SI-C3A
###

import board
import player
from ghosts import *
from board import draw_board
from game_over import *
from game_win import *

music = None

# Music for the game
def game_music():
    global music
    pygame.mixer.init()
    music = pygame.mixer.Sound("Assets/Sounds/Game.mp3")
    music.set_volume(0.5)
    music.play(loops=-1)  # -1 for infinite loop

# Title for the game windows
def game_title():
    # Title settings
    title_font = pygame.font.Font('Assets/PAC-FONT.TTF', 80)
    title_text = title_font.render('PAC-MAN', True, yellow, (0, 0, 0))
    title_text_rect = title_text.get_rect()
    title_text_rect.center = (window_width // 2, window_height // 12)
    screen.blit(title_text, title_text_rect)

# Window settings for the game
def game_settings():
    global player_images
    pygame.init()
    global screen, window_width, window_height
    window_width = 800
    window_height = 900

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("GAME PAC-MAN")
    game_icon = pygame.image.load('Icons/Joystick.png')
    pygame.display.set_icon(game_icon)
    player_images = player.load_player_images(case_size)

# Function to draw the number of lives on the screen
def draw_lives(screen, lives):
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f'Lives: {lives}', True, white)
    screen.blit(lives_text, (10, 825))

# Function to draw the score on the screen
def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (650, 825))

def game_loop():
    global tick

    # Variables for the game
    player_grid_x = player.starting_col
    player_grid_y = player.starting_row

    last_direction = 'right'

    current_image_index = 0
    frame_count = 0
    frame_limit = 5
    tick = 0
    pause_duration = 30
    pause_timer = 0
    score = 0

    is_paused = False
    game_over = False
    game_win = False

    ghost_images = load_ghost_images(player.case_size)
    ghosts = create_ghosts(board, ghost_images)  # Initialize ghosts

    running = True
    game_music()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)
        game_title()

        # Speed for the ghosts
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

        # Check for win condition
        if score >= 12300:
            game_win = True
            music.stop()

        # Check for loose condition
        if game_over:
            draw_game_over(screen)
            music.stop()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset game state
                player.lives = 3
                player_grid_x = player.starting_col
                player_grid_y = player.starting_row
                ghosts = create_ghosts(board, ghost_images)
                game_over = False
                game_music()

        # Check if the player has won
        elif game_win:
            draw_game_win(screen)

        else:
            # Get player movements and direction
            player_grid_x, player_grid_y, last_direction, moving = player.player_movements(
                pygame.key.get_pressed(), player_grid_x, player_grid_y, last_direction, frame_count)

            # Handle pause logic for not loosing lives in 1 s
            if is_paused:
                pause_timer += 1
                if pause_timer >= pause_duration:
                    is_paused = False
                    pause_timer = 0
            else:
                if player.check_collision(player_grid_x * player.case_size, player_grid_y * player.case_size, ghosts):
                    player.lives -= 1
                    is_paused = True

                # Check if player has no lives left
                if player.lives <= 0:
                    game_over = True

        # Draw the number of lives and score on the screen
        draw_lives(screen, player.lives)
        draw_score(screen, score)

        score = player.update_board_coins(board, player_grid_x, player_grid_y, score)

        # Update the player's animation based on position
        current_image_index, frame_count = player.player_animation(screen, player_images,
            player_grid_x * player.case_size, player_grid_y * player.case_size,
            current_image_index, frame_count, frame_limit, last_direction, tick, width, height)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    game_settings()
    game_loop()
