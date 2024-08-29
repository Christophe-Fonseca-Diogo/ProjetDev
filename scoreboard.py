###
# This file is for the game
# Last Edited : 28.08.2024
# Made by Christophe & Zachary
# SI-C3A
###

from dependencies import *


# Window settings for the scoreboard
def scoreboard_settings():
    pygame.init()
    global screen, window_width, window_height
    # Set up the window dimensions
    window_width = 800
    window_height = 800

    # Create the screen object
    screen = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption("Scoreboard PAC-MAN")

    # Set the icon of the window
    game_icon = pygame.image.load('Icons/Trophy.png')

    pygame.display.set_icon(game_icon)


# Main Text for the title
def title_scoreboard():

    # Title settings
    title_font = pygame.font.Font('Assets/PAC-FONT.TTF', 80)
    title_text = title_font.render('SCOREBOARD', True, yellow, (0, 0, 0))
    title_text_rect = title_text.get_rect()

    # set the center of the rectangular object.
    title_text_rect.center = (window_width // 2, window_height // 10)
    # show in the screen
    screen.blit(title_text, title_text_rect)

    pygame.display.update()


def rectangle():
    rect_x = (window_width // 2) - (window_height // 2)  # Center horizontally
    rect_y = (window_height // 10) - (window_height // 2)  # Set vertically with a slight

    color = blue

    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(30,30,30,30))
    pygame.display.flip()


# Loop for the scoreboard
def scoreboard_loop():
    running = True
    title_scoreboard()
    rectangle()
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Update the screen
    pygame.display.update()


if __name__ == "__main__":
    # Main windows settings
    scoreboard_settings()

    # Using the loop for the scoreboard
    scoreboard_loop()
