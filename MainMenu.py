###
# This file is for the Main Menu of our game : Pac Man
# Last Edited :
# Made by Christophe & Zachary
# SI-C3A
###

from Dependencies import *

pygame.init()
# Set up the window dimensions
window_width = 800
window_height = 600

# Create the screen object
screen = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Pac Man by Christophe & Zachary")

# Set the icon of the window
gameicon = pygame.image.load('Assets/Icon.png')

pygame.display.set_icon(gameicon)

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

        # Update the display
        pygame.display.flip()


# Using the loop for the game
main_loop()

# Quit Pygame
pygame.quit()