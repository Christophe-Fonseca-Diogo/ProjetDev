###
# This file is for the Main Menu of our game : Pac-Man
# Last Edited :
# Made by Christophe & Zachary
# SI-C3A
###
import pygame.font

from Dependencies import *


def main_settings():
    pygame.init()
    global screen, window_width, window_height
    # Set up the window dimensions
    window_width = 800
    window_height = 800

    # Create the screen object
    screen = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption("Pac Man by Christophe & Zachary")

    # Set the icon of the window
    game_icon = pygame.image.load('Assets/Icon.png')

    pygame.display.set_icon(game_icon)


def texts_main_menu():

    pygame.font.init()

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
    copyrights_text = copyrights_font.render('1 Made by Christophe and Zachary 9', True, red, (0, 0, 0))
    copyrights_text_rect = copyrights_text.get_rect()

    # set the center of the rectangular object.
    copyrights_text_rect.center = (window_width // 2, window_height // 4)

    # show in the screen
    screen.blit(copyrights_text, copyrights_text_rect)


# Main loop
def main_loop():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color (RGB)
        screen.fill((0, 0, 0))  # Fill the screen with black

        texts_main_menu()

        # Update the display
        pygame.display.flip()


# Main windows settings
main_settings()

# Using the loop for the game
main_loop()

# Quit Pygame
pygame.quit()
