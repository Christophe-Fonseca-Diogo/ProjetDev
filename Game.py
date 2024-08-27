###
# This file is for the game
# Last Edited :
# Made by Christophe & Zachary
# SI-C3A
###

from Dependencies import *


def game_settings():
    pygame.init()
    global screen, window_width, window_height
    # Set up the window dimensions
    window_width = 800
    window_height = 200

    # Create the screen object
    screen = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption("Pac Man by Christophe & Zachary 2")

    # Set the icon of the window
    game_icon = pygame.image.load('Assets/Icon.png')

    pygame.display.set_icon(game_icon)


def game_loop():
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



if __name__=="__main__":
    # Main windows settings
    game_settings()

    # Using the loop for the game
    game_loop()

    pygame.quit()