###
# This file is for all the settings for the game win
# Last Edited : 28.10.2024
# Made by Christophe & Zachary
# SI-C3A
###

from dependencies import *

# Variable for the sound
game_win_sound_played = False

# Function for the game over sound
def game_win_sound():
    pygame.mixer.init()
    game_win_sound = pygame.mixer.Sound("Assets/Sounds/game_win_sound.mp3")
    game_win_sound.set_volume(0.8)
    game_win_sound.play()

# Function to display game win
def draw_game_win(screen):
    font = pygame.font.Font(None, 100)
    game_win_text = font.render('GAME WIN', True, white)
    screen.blit(game_win_text, (800 // 2 - game_win_text.get_width() // 2, 800 // 2.2))

    global game_win_sound_played
    if not game_win_sound_played:
        game_win_sound()
        game_win_sound_played = True