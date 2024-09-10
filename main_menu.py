###
# This file is for the Main Menu of our game : Pac-Man
# Last Edited : 06.09.2024
# Made by Christophe & Zachary
# SI-C3A
###
import pygame.mixer

from dependencies import *
from game import game_loop, game_settings
from scoreboard import scoreboard_loop, scoreboard_settings, button_back

Screen = "Main"
# Music for the menu
def menu_music():
    pygame.mixer.init()
    music = pygame.mixer.Sound("Assets/Sounds/Main_Menu.mp3")
    # -1 for infinite loop
    music.play(loops=-1)


# Settings for the window
def main_settings():
    pygame.init()
    pygame.font.init()
    global screen, window_width, window_height
    # Set up the window dimensions
    window_width = 800
    window_height = 800

    # Create the screen object
    screen = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption("Pac Man by Christophe & Zachary")

    # Set the icon of the window
    game_icon = pygame.image.load('Icons/Icon_Pac.png')

    pygame.display.set_icon(game_icon)
    pygame.display.update()


# Main Text for the title
def texts_main_menu():

    # Title settings
    title_font = pygame.font.Font('Assets/PAC-FONT.TTF', 80)
    title_text = title_font.render('PAC-MAN', True, yellow, (0, 0, 0))
    title_text_rect = title_text.get_rect()

    # set the center of the rectangular object.
    title_text_rect.center = (window_width // 2, window_height // 10)
    # show in the screen
    screen.blit(title_text, title_text_rect)

    # copyrights settings
    copyrights_font = pygame.font.Font('Assets/PAC-FONT.TTF', 25)
    copyrights_text = copyrights_font.render('1 00000000000000000000000000000000000000000000000000000000000000000 9', True, red, (0, 0, 0))
    copyrights_text_rect = copyrights_text.get_rect()

    # set the center of the rectangular object.
    copyrights_text_rect.center = (window_width // 2, window_height // 4)

    # show in the screen
    screen.blit(copyrights_text, copyrights_text_rect)

    pygame.display.update()


# Button settings for starting the game
def button_play():

    # Draw button
    button_play_font = pygame.font.Font('Assets/2FONT.ttf', 40)
    button_play_text = button_play_font.render('‎ ‎ ‎ START ‎ ‎ ‎', True, black)
    button_play_rect = button_play_text.get_rect()
    button_play_rect.center = (window_width // 2, window_height // 2.5)

    # Background of the rectangle
    pygame.draw.rect(screen, yellow, button_play_rect)
    # Text in the rectangle
    screen.blit(button_play_text, button_play_rect)
    # Event handling
    return button_play_rect


# Button settings for leaving the game
def button_exit():

    # Draw button
    button_exit_font = pygame.font.Font('Assets/2FONT.ttf', 40)
    button_exit_text = button_exit_font.render('‎ EXIT ‎', True, black)
    button_exit_rect = button_exit_text.get_rect()
    button_exit_rect.center = (window_width // 2, window_height // 1.5)

    # Background of the rectangle
    pygame.draw.rect(screen, red, button_exit_rect)
    # Text in the rectangle
    screen.blit(button_exit_text, button_exit_rect)
    # Event handling
    return button_exit_rect


# Button settings for leaving the game
def button_scoreboard():

    # Draw button
    button_scoreboard_font = pygame.font.Font('Assets/2FONT.ttf', 40)
    button_scoreboard_text = button_scoreboard_font.render('‎ SCOREBOARD ‎', True, black)
    button_scoreboard_rect = button_scoreboard_text.get_rect()
    button_scoreboard_rect.center = (window_width // 2, window_height // 1.9)

    # Background of the rectangle
    pygame.draw.rect(screen, blue, button_scoreboard_rect)
    # Text in the rectangle
    screen.blit(button_scoreboard_text, button_scoreboard_rect)
    # Event handling
    return button_scoreboard_rect


# Main loop for the menu
def main_loop():
    global Screen
    running = True
    texts_main_menu()
    button_play_rect = button_play()
    button_exit_rect = button_exit()
    button_scoreboard_rect = button_scoreboard()
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button

                    if button_play_rect.collidepoint(event.pos):
                        # Quit the menu
                        pygame.quit()
                        # Settings for the game
                        game_settings()
                        # Game function
                        game_loop()
                        # Stop the loop of the menu
                        running = False

                    if button_exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

                    if button_scoreboard_rect.collidepoint(event.pos):
                        Screen = "Scoreboard"
                        # Settings for the scoreboard
                        scoreboard_settings()
                        scoreboard_loop()
                        # Stop the loop of the menu
                        running = False

                    if Screen == "Scoreboard":
                        if button_back():
                            Screen = "Main"
                            main_settings()
                            main_loop()
                            running = False

        # Update the screen
        pygame.display.update()


if __name__ == "__main__":
    # Main windows settings
    main_settings()
    # Background music for the menu
    menu_music()
    # Using the loop for the menu
    main_loop()
