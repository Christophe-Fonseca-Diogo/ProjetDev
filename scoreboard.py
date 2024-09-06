###
# This file is for the game
# Last Edited : 06.09.2024
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
    title_text_rect.center = (window_width // 2, window_height // 9)
    # show in the screen
    screen.blit(title_text, title_text_rect)

    pygame.display.update()


# Blue rectangle for the scoreboard
def rectangle():
    # Define rectangle properties
    rect_width = 300
    rect_height = 400
    rect_x = (window_width // 2) - (rect_width // 2)  # Center horizontally
    rect_y = (window_height // 2) - (rect_height // 2)  # Center vertically
    rectangle_color = blue
    pygame.draw.rect(screen, rectangle_color, (rect_x, rect_y, rect_width, rect_height), border_radius=50)
    # Update the screen
    pygame.display.update()


# Button for going back in the menu
def button_back():

    # Draw button
    button_back_font = pygame.font.Font('Assets/2FONT.ttf', 40)
    button_back_text = button_back_font.render('‎ BACK ‎', True, black)
    button_back_rect = button_back_text.get_rect()
    button_back_rect.center = (window_width // 2, window_height // 1.1)

    # Background of the rectangle
    pygame.draw.rect(screen, red, button_back_rect)
    # Text in the rectangle
    screen.blit(button_back_text, button_back_rect)
    # Event handling
    return button_back_rect


# Loop for the scoreboard
def scoreboard_loop():
    running = True
    button_back_rect = button_back()
    title_scoreboard()
    rectangle()

    # Update the screen immediately after drawing the necessary elements
    pygame.display.update()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if button_back_rect.collidepoint(event.pos):
                        running = False  # Exit the scoreboard loop

        # Update the screen inside the loop
        pygame.display.update()


if __name__ == "__main__":
    # Main windows settings
    scoreboard_settings()

    # Using the loop for the scoreboard
    scoreboard_loop()
