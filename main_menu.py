###
# This file is for the Main Menu of our game : Pac-Man
# Last Edited :
# Made by Christophe & Zachary
# SI-C3A
###
import pygame.display

from dependencies import *
from game import game_loop

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
    pygame.display.update()

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


def button_play():

    # Draw button
    button_play_font = pygame.font.Font('Assets/2FONT.ttf', 40)
    button_play_text = button_play_font.render('‎ ‎ ‎ START ‎ ‎ ‎', True, black)
    button_play_rect = button_play_text.get_rect()
    button_play_rect.center = (window_width // 2, window_height // 2.5)

    pygame.draw.rect(screen, yellow, button_play_rect)  # Draw background
    screen.blit(button_play_text, button_play_rect)  # Draw button text
    return button_play_rect  # Return the button rectangle for event handling


def button_event_game(button_play_rect):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button_play_rect.collidepoint(event.pos):
                    game_loop()


def button_exit():

    # Draw button
    button_exit_font = pygame.font.Font('Assets/2FONT.ttf', 40)
    button_exit_text = button_exit_font.render('‎ EXIT ‎', True, black)
    button_exit_rect = button_exit_text.get_rect()
    button_exit_rect.center = (window_width // 2, window_height // 1.5)

    pygame.draw.rect(screen, red, button_exit_rect)  # Draw background
    screen.blit(button_exit_text, button_exit_rect)  # Draw button text
    return button_exit_rect  # Return the button rectangle for event handling


def button_event_quit(button_exit_rect):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button_exit_rect.collidepoint(event.pos):
                    exit()

# Main loop
def main_loop():
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw buttons and handle events
        button_play_rect = button_play()
        button_exit_rect = button_exit()
        # Display the main menu texts
        texts_main_menu()


 #       button_event_game(button_play_rect)
        button_event_quit(button_exit_rect)  # Handle exit event

if __name__=="__main__":
    # Main windows settings
    main_settings()

    # Using the loop for the menu
    main_loop()