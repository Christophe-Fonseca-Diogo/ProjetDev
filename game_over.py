###
# This file is for all the settings for the game over
# Last Edited : 27.10.2024
# Made by Christophe & Zachary
# SI-C3A
###

from dependencies import *

# Variable for the sound
game_over_sound_played = False

# Function for the game over sound
def game_over_sound():
    pygame.mixer.init()
    coin_pickup_sound = pygame.mixer.Sound("Assets/Sounds/game_over_sound.mp3")
    coin_pickup_sound.set_volume(0.8)
    coin_pickup_sound.play()

# Function to display game over
def draw_game_over(screen):
    font = pygame.font.Font(None, 74)  # Font for game over
    game_over_text = font.render('GAME OVER', True, red)
    restart_text = font.render('Press R to Restart', True, red)
    screen.blit(game_over_text, (800 // 2 - game_over_text.get_width() // 2, 900 // 3))
    screen.blit(restart_text, (800 // 2 - restart_text.get_width() // 2, 900 // 2))

    global game_over_sound_played
    if not game_over_sound_played:
        game_over_sound()
        game_over_sound_played = True
