###
# This file is for the game
# Last Edited : 06.09.2024
# Made by Christophe & Zachary
# SI-C3A
###

import player
from dependencies import *

# Music for the game
def game_music():
    pygame.mixer.init()
    music = pygame.mixer.Sound("Assets/Sounds/Game.mp3")
    # -1 for infinite loop
    music.play(loops=-1)

# Window settings for the game
def game_settings():
    global player_images, character
    pygame.init()
    global screen, window_width, window_height
    # Set up the window dimensions
    window_width = 800
    window_height = 800

    # Create the screen object
    screen = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption("GAME PAC-MAN")

    # Set the icon of the window
    game_icon = pygame.image.load('Icons/Joystick.png')

    pygame.display.set_icon(game_icon)
    player_images = player.load_player_images(100, 100)
    character = player.draw_player(screen, player_images, window_width, window_height, 0)


# Loop for the game
def game_loop():
    running = True
    game_music()
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    # Main windows settings
    game_settings()

    # Using the loop for the game
    game_loop()
