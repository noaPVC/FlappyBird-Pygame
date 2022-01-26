import pygame
from pygame import mixer
import os


pygame.init()
mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 577, 780
WHITE = (255, 255, 255)

BTN_SIZE = 100
BTN_SMALL_SIZE = 60

frame_icon = pygame.image.load(
    os.path.join('vis/assets/icon', 'frame_icon.png'))
# imgs
BG_DAY = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/bgs', 'background-day.png')), (WIDTH, HEIGHT))

BG_NIGHT = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/bgs', 'background-night.png')), (WIDTH, HEIGHT))


# animation frames

# BIRD FRAMES

# bluebird
bluebird_f_1 = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/bird', 'bluebird-upflap.png')))
bluebird_f_2 = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/bird', 'bluebird-midflap.png')))
bluebird_f_3 = pygame.transform.scale2x(pygame.image.load(os.path.join(
    'vis/assets/bird', 'bluebird-downflap.png')))

# redbird
redbird_f_1 = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/bird', 'redbird-upflap.png')))
redbird_f_2 = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/bird', 'redbird-midflap.png')))
redbird_f_3 = pygame.transform.scale2x(pygame.image.load(os.path.join(
    'vis/assets/bird', 'redbird-downflap.png')))

# yellowbird
yellowbird_f_1 = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/bird', 'yellowbird-upflap.png')))
yellowbird_f_2 = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/bird', 'yellowbird-midflap.png')))
yellowbird_f_3 = pygame.transform.scale2x(pygame.image.load(os.path.join(
    'vis/assets/bird', 'yellowbird-downflap.png')))

# PIPES

RED_PIPE = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/pipes', 'pipe-red.png')))
GREEN_PIPE = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/pipes', 'pipe-green.png')))


# OTHER MATERIAL

base_img = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets', 'base.png')), (WIDTH, 200))
gameover_img = pygame.transform.scale2x(
    pygame.image.load(os.path.join('vis/assets', 'gameover.png')))

# home menu
title_img = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets', 'flappy_bird_title_img.png')), (380, 100))

# help screen imgs
tap_img = pygame.transform.scale2x(pygame.image.load(
    os.path.join('vis/assets/help_screen_assets', 'tap_to_jump.png')))

help_title = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/help_screen_assets', 'title_help.png')), (400, 80))

collision_sign = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/help_screen_assets', 'collision_sign.png')), (130, 110))

txt1 = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/help_screen_assets', 'text_explain_1.png')), (420, 120))

txt2 = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/help_screen_assets', 'text_explain_2.png')), (420, 120))

# audio
main_theme = mixer.music.load(os.path.join(
    'vis/audio', 'flappy_main_theme.mp3'))

# SFX
point_sfx = pygame.mixer.Sound(os.path.join('vis/audio/sfx', 'sfx_point.wav'))
wing_sfx = pygame.mixer.Sound(os.path.join('vis/audio/sfx', 'sfx_wing.wav'))
swooshing_sfx = pygame.mixer.Sound(
    os.path.join('vis/audio/sfx', 'sfx_swooshing.wav'))

# font
main_game_font = pygame.font.Font('vis/font/game_font.ttf', 40)
info_font = pygame.font.Font('vis/font/game_font.ttf', 21)
regular_font = pygame.font.Font('vis/font/game_font.ttf', 35)
settings_font = pygame.font.Font('vis/font/game_font.ttf', 38)
settings_title_font = pygame.font.Font('vis/font/game_font.ttf', 70)

big_font = pygame.font.Font('vis/font/game_font.ttf', 80)
