###
# This file is for the game
# Last Edited : 28.08.2024
# Made by Christophe & Zachary
# SI-C3A
###

from dependencies import *


# Window settings for the game
def game_settings():
    pygame.init()
    global screen, window_width, window_height
    # Set up the window dimensions
    window_width = 800
    window_height = 200

    # Create the screen object
    screen = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption("GAME PAC-MAN")

    # Set the icon of the window
    game_icon = pygame.image.load('Icons/Joystick.png')

    pygame.display.set_icon(game_icon)


# Loop for the game
def game_loop():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    # Main windows settings
    game_settings()

    # Using the loop for the game
    game_loop()
