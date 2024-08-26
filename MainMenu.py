###
# This file is for the Main Menu of our game : Pac-Man
# Last Edited :
# Made by Christophe & Zachary
# SI-C3A
###

from Dependencies import *


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
    game_icon = pygame.image.load('Assets/Icon.png')

    pygame.display.set_icon(game_icon)


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
    copyrights_text = copyrights_font.render('1 Made by Christophe and Zachary 9', True, red, (0, 0, 0))
    copyrights_text_rect = copyrights_text.get_rect()

    # set the center of the rectangular object.
    copyrights_text_rect.center = (window_width // 2, window_height // 4)

    # show in the screen
    screen.blit(copyrights_text, copyrights_text_rect)


def button_play():

    # Draw button
    button_font = pygame.font.Font('Assets/PAC-FONT.TTF', 40)
    button_text = button_font.render('Start', True, black)
    button_rect = button_text.get_rect()
    button_rect.center = (window_width // 2, window_height // 2)

    pygame.draw.rect(screen, yellow, button_rect)  # Draw background
    screen.blit(button_text, button_rect)  # Draw button text
    return button_rect  # Return the button rectangle for event handling


def button_event_game(button_rect):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button_rect.collidepoint(event.pos):
                    from Game import game_loop
                    game_loop()


# Main loop
def main_loop():
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        button_rect = button_play()
        # display the text
        texts_main_menu()
        #
        button_event_game(button_rect)

        # Update the display
        pygame.display.flip()


# Main windows settings
main_settings()

# Using the loop for the menu
main_loop()

pygame.quit()
